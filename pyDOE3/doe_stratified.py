import itertools
import math
import random
import sys
import numpy as np


def unitcube(dimension):
    """Shortcut to generate a tuple of bounds of the unit hypercube."""
    assert dimension > 0
    return [0.0] * dimension, [1.0] * dimension


def stratify_conventional(num_strata, dimension):
    """Stratification of the unit hypercube.

    This algorithm divides the hypercube into `num_points` subcells and
    draws a random uniform point from each cell. Thus, the result is
    stochastic, but more uniform than a random uniform sample. For further
    information see [McKay1979]_.

    Parameters
    ----------
    num_strata : int
        The number of strata to generate.
        ``num_strata ** (1/dimension)`` must be integer.
    dimension : int
        The dimension of the space.

    Returns
    -------
    strata : list of tuple
        As the strata are axis-aligned boxes in this case, each tuple in
        the returned list contains the lower and upper corner of a stratum.

    """
    # shortcuts & initialization
    assert num_strata > 0
    assert dimension > 0
    points_per_axis = int(num_strata ** (1.0 / dimension))
    if points_per_axis**dimension != num_strata:
        points_per_axis += 1
    assert points_per_axis**dimension == num_strata
    final_strata = []
    extent = 1.0 / points_per_axis
    possible_values = [float(x) / points_per_axis for x in range(points_per_axis)]
    # calculate grid cells and sample
    for lower_bounds in itertools.product(possible_values, repeat=dimension):
        upper_bounds = [lower + extent for lower in lower_bounds]
        final_strata.append((list(lower_bounds), upper_bounds))
    return final_strata


def stratify_generalized(
    num_strata, dimension, cuboid=None, detect_special_case=True, avoid_odd_numbers=True
):
    """Generalized stratification of the unit hypercube.

    The adjective "generalized" pertains to the fact that the number of
    strata can be chosen arbitrarily, which is not possible with
    :func:`stratify_conventional`. It is guaranteed that all strata have
    volume ``volume(cuboid) / num_strata``, apart from rounding error.

    Parameters
    ----------
    num_strata : int
        The number of strata to generate. An arbitrary number of points
        is possible for this algorithm.
    dimension : int
        The dimension of the search space.
    cuboid : tuple of list, optional
        Optionally specify the hypercube to be sampled in. If None, the
        unit hypercube is chosen.
    detect_special_case : bool, optional
        If True, ``num_points ** (1/dimension)`` is integer, and we are
        sampling the unit cube, use the original stratified sampling in
        :func:`stratify_conventional`.
    avoid_odd_numbers : bool, optional
        If this value is True, splits are chosen so that the resulting
        numbers are even, whenever possible. E.g., if a stratum with six
        points is splitted, it is not split into three and three, but two
        and four points. For more information on this option, see
        [Wessing2018]_.

    Returns
    -------
    strata : list of tuple
        As the strata are axis-aligned boxes in this case, each tuple in
        the returned list contains the lower and upper corner of a stratum.

    References
    ----------
    .. [Wessing2018] Wessing, Simon (2018). Experimental Analysis of a
        Generalized Stratified Sampling Algorithm for Hypercubes. arXiv
        eprint 1705.03809. https://arxiv.org/abs/1705.03809

    """
    # sanity checks
    assert num_strata > 0
    assert dimension > 0
    if cuboid is None:
        cuboid = unitcube(dimension)
    assert len(cuboid[0]) == dimension
    assert len(cuboid[1]) == dimension
    # special case
    if detect_special_case and cuboid == unitcube(dimension):
        points_per_axis = int(num_strata ** (1.0 / dimension))
        is_integer_power = points_per_axis**dimension == num_strata
        # check because of potential rounding error:
        is_integer_power |= (points_per_axis + 1) ** dimension == num_strata
        if is_integer_power:
            return stratify_conventional(num_strata, dimension)
    # more initialization
    dimensions = list(range(dimension))
    final_strata = []
    remaining_strata = [(num_strata, cuboid)]
    # begin partitioning
    while remaining_strata:
        current_num_points, current_bounds = remaining_strata.pop()
        if current_num_points == 1:
            final_strata.append(current_bounds)
            continue
        current_lower, current_upper = current_bounds
        diffs = [current_upper[i] - current_lower[i] for i in dimensions]
        max_extent = max(diffs)
        max_extent_dims = [i for i in dimensions if diffs[i] == max_extent]
        num1 = int(current_num_points * 0.5)
        do_subtract_one = avoid_odd_numbers and current_num_points >= 6
        do_subtract_one &= num1 % 2 != 0 and current_num_points % 2 == 0
        if do_subtract_one:
            num1 -= 1
        num2 = current_num_points - num1
        if random.random() < 0.5:
            num1, num2 = num2, num1
        split_dim = random.choice(max_extent_dims)
        split_pos = float(num1) / current_num_points
        split_pos = current_lower[split_dim] + max_extent * split_pos
        new_upper = current_upper[:]
        new_upper[split_dim] = split_pos
        new_lower = current_lower[:]
        new_lower[split_dim] = split_pos
        stratum1 = (num1, (current_lower, new_upper))
        stratum2 = (num2, (new_lower, current_upper))
        remaining_strata.extend((stratum1, stratum2))
    return final_strata


def stratified_sampling(
    strata, bates_param=1, latin="none", matching_init="approx", full_output=False
):
    """Stratified sampling with given strata.

    Parameters
    ----------
    strata : list of tuple
        The strata to be sampled. Each tuple in the list must contain the
        lower and upper corner of a stratum.
    bates_param : int, optional
        Each coordinate of a point sampled in a stratum is determined as
        the mean of this number of independent random uniform variables.
        Thus, the coordinates follow the Bates distribution.
    latin : str, optional
        Indicates if and how the point set should be latinized. "none" is
        the fastest option, sampling the points in linear time without
        latinization. "approx" uses a heuristic with runtime
        :math:`O(nN \\log N)` that may produce a slightly imperfect
        latinization. "matching" produces an error-free latinization using
        a maximum cardinality matching algorithm with runtime
        :math:`O(nN^2)`. The union of the strata must be the unit hypercube
        for the second and third option to work.
    matching_init : str, optional
        This is an additional option to the setting ``latin == "matching"``.
        Firstly, the approximative latinization from ``latin == "approx"`` can
        be used as initialization for the matching algorithm, with the
        matching acting as a repair method if necessary. This is the
        recommended choice due to its favorable runtime behavior.
        The other two options use a problem-agnostic greedy initialization.
        "greedy-rand" randomly shuffles the edges in the bipartite
        graph data structure. This order indirectly influences the
        distribution of the point sample, via the deterministic matching
        algorithm. "greedy-det" is the deterministic variant without extras,
        which may produce patterns due to the deterministic nature of the
        algorithm.
    full_output : bool, optional
        Indicates if the indices of points with latin hypercube violations
        are returned in case of latinized sampling.

    Returns
    -------
    points : numpy array
        The sampled points, in corresponding order to `strata`.
    error_indices : set
        Indices of points with violations of the latin hypercube property
        in some dimension. Can only be non-empty for ``latin == "approx"``.

    """

    def bipartite_match(graph, matching=None):
        """Find maximum cardinality matching of a bipartite graph (U, V, E).

        The input format is a dictionary mapping members of U to a list
        of their neighbors in V.  The output is a triple (M, A, B) where M
        is a dictionary mapping members of V to their matches in U, A is
        the part of the maximum independent set in U, and B is the part of
        the MIS in V. The same object may occur in both U and V, and is
        treated as two distinct vertices if this happens.

        Adapted from
        https://github.com/ActiveState/code/tree/master/recipes/Python/123641_HopcroftKarp_bipartite_matching
        Hopcroft-Karp bipartite max-cardinality matching and max independent set
        David Eppstein, UC Irvine, 27 Apr 2002

        """
        if not matching:
            # initialize greedy matching (redundant, but faster than full search)
            matching = {}
            for u in graph:
                for v in graph[u]:
                    if v not in matching:
                        matching[v] = u
                        break
        while True:
            # structure residual graph into layers
            # pred[u] gives the neighbor in the previous layer for u in U
            # preds[v] gives a list of neighbors in the previous layer for v in V
            # unmatched gives a list of unmatched vertices in final layer of V,
            # and is also used as a flag value for pred[u] when u is in the first layer
            preds = {}
            unmatched = []
            pred = dict([(u, unmatched) for u in graph])
            for v in matching:
                del pred[matching[v]]
            layer = list(pred)
            # repeatedly extend layering structure by another pair of layers
            while layer and not unmatched:
                new_layer = {}
                for u in layer:
                    for v in graph[u]:
                        if v not in preds:
                            new_layer.setdefault(v, []).append(u)
                layer = []
                for v in new_layer:
                    preds[v] = new_layer[v]
                    if v in matching:
                        layer.append(matching[v])
                        pred[matching[v]] = v
                    else:
                        unmatched.append(v)
            # did we finish layering without finding any alternating paths?
            if not unmatched:
                unlayered = {}
                for u in graph:
                    for v in graph[u]:
                        if v not in preds:
                            unlayered[v] = None
                return matching, list(pred), list(unlayered)

            # recursively search backward through layers to find alternating paths
            # recursion returns true if found path, false otherwise
            def recurse(v):
                if v in preds:
                    L = preds[v]
                    del preds[v]
                    for u in L:
                        if u in pred:
                            pu = pred[u]
                            del pred[u]
                            if pu is unmatched or recurse(pu):
                                matching[v] = u
                                return 1
                return 0

            for v in unmatched:
                recurse(v)

    # sanity checks & initialization
    assert len(strata) > 0
    assert bates_param > 0
    assert latin != "matching" or matching_init in (
        "approx",
        "greedy-det",
        "greedy-rand",
    )
    num_points = len(strata)
    dimension = len(strata[0][0])
    points = np.empty((num_points, dimension))
    rand_uni = random.uniform
    error_indices = set()
    if latin == "none":
        for dim_index in range(dimension):
            for j, stratum in enumerate(strata):
                low, high = stratum[0][dim_index], stratum[1][dim_index]
                if math.isinf(bates_param):
                    points[j][dim_index] = (low + high) * 0.5
                elif bates_param == 1:
                    points[j][dim_index] = rand_uni(low, high)
                else:
                    uniform_sum = sum(rand_uni(low, high) for _ in range(bates_param))
                    points[j][dim_index] = uniform_sum / bates_param
    else:
        bin_size = 1.0 / num_points
        for dim_index in range(dimension):

            def cog_key(strat_idx):
                """Two times the center of gravity."""
                stratum = strata[strat_idx]
                return stratum[0][dim_index] + stratum[1][dim_index]

            strat_indices = np.random.permutation(num_points).tolist()
            strat_indices.sort(key=cog_key)
            bin_indices = list(range(num_points))
            if latin == "approx":
                # strat_indices has already been sorted above
                pass
            elif latin == "matching":
                dim_graph = {}
                matching = {}
                for bin_idx, strat_idx in zip(bin_indices, strat_indices):
                    stratum = strata[strat_idx]
                    low, high = stratum[0][dim_index], stratum[1][dim_index]
                    low_bin = int(low / bin_size)
                    high_bin = int(math.ceil(high / bin_size))
                    avail_bins = np.arange(low_bin, high_bin)
                    if matching_init == "approx" and bin_idx in avail_bins:
                        matching[bin_idx] = strat_idx
                    elif matching_init == "greedy-rand":
                        np.random.shuffle(avail_bins)
                    dim_graph[strat_idx] = avail_bins
                if len(matching) < num_points:
                    matching, max_ind_set, _ = bipartite_match(dim_graph, matching)
                    assert len(max_ind_set) == 0
                    bin_indices = matching.keys()
                    strat_indices = matching.values()
            else:
                raise Exception("unknown latin hypercube option " + str(latin))
            for bin_idx, strat_idx in zip(bin_indices, strat_indices):
                stratum = strata[strat_idx]
                low, high = stratum[0][dim_index], stratum[1][dim_index]
                low2, high2 = bin_idx * bin_size, (bin_idx + 1) * bin_size
                low, high = max(low, low2), min(high, high2)
                if not high >= low:
                    error_indices.add(strat_idx)
                    # revert to uniform sampling of the stratum in this dim
                    low, high = stratum[0][dim_index], stratum[1][dim_index]
                if math.isinf(bates_param):
                    points[strat_idx][dim_index] = (low + high) * 0.5
                elif bates_param == 1:
                    points[strat_idx][dim_index] = rand_uni(low, high)
                else:
                    uniform_sum = sum(rand_uni(low, high) for _ in range(bates_param))
                    points[strat_idx][dim_index] = uniform_sum / bates_param
    if full_output:
        return points, error_indices
    else:
        return points


def reconstruct_strata_from_points(points, cuboid=None):
    """Partitions the cuboid so that each point has its own hyperbox.

    This partitioning is stochastic (ties are broken randomly). The obtained
    strata will have different volumes. This function can be used to
    calculate an upper bound for the covering radius of arbitrary point
    sets via
    :func:`covering_radius_upper_bound()<diversipy.indicator.covering_radius_upper_bound>`.
    The idea for this approach was introduced in [Wessing2018]_.

    Parameters
    ----------
    points : sequence of sequence
        The sampled points.
    cuboid : tuple of list, optional
        Optionally specify the outer bounds of the partitioning. If None,
        the unit hypercube is chosen.

    Returns
    -------
    strata : list of tuple
        As the strata are axis-aligned boxes in this case, each tuple in
        the returned list contains the lower and upper corner of a stratum.
        The order corresponds to the order of `points`.

    """
    dimension = len(points[0])
    dimensions = list(range(dimension))
    if cuboid is None:
        cuboid = unitcube(dimension)
    assert len(cuboid[0]) == dimension
    assert len(cuboid[1]) == dimension
    for point in points:
        assert np.all(point >= cuboid[0]) and np.all(point <= cuboid[1])
    final_strata = dict()
    remaining_strata = [(points, cuboid)]
    while remaining_strata:
        current_points, current_bounds = remaining_strata.pop()
        if len(current_points) == 1:
            final_strata[tuple(current_points[0])] = current_bounds
            continue
        current_lower, current_upper = current_bounds
        diffs = [current_upper[i] - current_lower[i] for i in dimensions]
        points_diffs = np.max(current_points, axis=0) - np.min(current_points, axis=0)
        combined_diffs = np.array(diffs)
        # filter out dimensions where all point coordinates coincide,
        # because we cannot obtain a non-empty stratum by splitting in this dimension
        combined_diffs[points_diffs == 0] = 0
        max_extent = max(combined_diffs)
        max_extent_dims = [i for i in dimensions if combined_diffs[i] == max_extent]
        split_dim = random.choice(max_extent_dims)
        prelim_split_pos = np.mean(current_points[:, split_dim])
        split_bit_mask = current_points[:, split_dim] < prelim_split_pos
        less_indices = np.where(split_bit_mask)[0]
        greater_equal_indices = np.where(1 - split_bit_mask)[0]
        # try to ensure we have points on either side of the split position by moving it
        if len(less_indices) == 0:
            min_index = np.argmin(current_points[greater_equal_indices, split_dim])
            prelim_split_pos = (
                current_points[min_index, split_dim] + sys.float_info.epsilon
            )
            split_bit_mask = current_points[:, split_dim] < prelim_split_pos
            less_indices = np.where(split_bit_mask)[0]
            greater_equal_indices = np.where(1 - split_bit_mask)[0]
        elif len(greater_equal_indices) == 0:
            max_index = np.argmax(current_points[less_indices, split_dim])
            prelim_split_pos = current_points[max_index, split_dim]
            split_bit_mask = current_points[:, split_dim] < prelim_split_pos
            less_indices = np.where(split_bit_mask)[0]
            greater_equal_indices = np.where(1 - split_bit_mask)[0]
        assert len(less_indices) > 0
        assert len(greater_equal_indices) > 0
        # finally identify nearest neighbors to split position in 1-D projection
        max_index = np.argmax(current_points[less_indices, split_dim])
        max_index = less_indices[max_index]
        min_index = np.argmin(current_points[greater_equal_indices, split_dim])
        min_index = greater_equal_indices[min_index]
        # center split position between these two points
        split_pos = (
            current_points[max_index, split_dim] + current_points[min_index, split_dim]
        ) * 0.5
        # create new strata
        new_upper = current_upper[:]
        new_upper[split_dim] = split_pos
        new_lower = current_lower[:]
        new_lower[split_dim] = split_pos
        stratum1 = (current_points[less_indices], (current_lower, new_upper))
        stratum2 = (current_points[greater_equal_indices], (new_lower, current_upper))
        remaining_strata.extend((stratum1, stratum2))
    final_strata = [final_strata[tuple(point)] for point in points]
    return final_strata

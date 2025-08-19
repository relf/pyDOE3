import numpy as np

from pyDOE3.utils.distance import calc_euclidean_dist_matrix
from pyDOE3.stratified_sampling_designs import (
    stratified_sampling,
    stratify_generalized,
)

__all__ = ["random_k_means"]

# NOTE:
# This source code is derived from Diversipy:
# https://www.simonwessing.de/diversipy/doc/


def random_k_means(
    num_points,
    dimension,
    num_steps=None,
    initial_points=None,
    dist_matrix_function=None,
    callback=None,
):
    """MacQueen's method.

    In its default setup, this algorithm converges to a centroidal Voronoi
    tesselation of the unit hypercube. Further information is given in
    [MacQueen1967]_.

    Parameters
    ----------
    num_points : int
        The number of points to generate.
    dimension : int
        The dimension of the space.
    num_steps : int, optional
        The number of iterations to carry out. Default is
        ``100 * num_points``.
    initial_points : array_like, optional
        The point set to improve (if None, a sample is drawn with
        :func:`stratified_sampling`).
    dist_matrix_function : callable, optional
        The function to compute the distances. Default is Euclidean
        distance.
    callback : callable, optional
        If provided, it is called in each iteration with the current point
        set as argument for monitoring progress.

    Returns
    -------
    cluster_centers : (`num_points`, `dimension`) numpy array

    References
    ----------
    .. [MacQueen1967] MacQueen, J. Some methods for classification and
        analysis of multivariate observations. Proceedings of the Fifth
        Berkeley Symposium on Mathematical Statistics and Probability,
        Volume 1: Statistics, pp. 281--297, University of California Press,
        Berkeley, Calif., 1967.
        http://projecteuclid.org/euclid.bsmsp/1200512992.

    """
    # initialization
    if num_steps is None:
        num_steps = 100 * num_points
    if initial_points is None:
        cluster_centers = stratified_sampling(
            stratify_generalized(num_points, dimension)
        )
    elif len(initial_points) == num_points:
        cluster_centers = np.array(initial_points)
        assert np.all(cluster_centers >= 0.0)
        assert np.all(cluster_centers <= 1.0)
    else:
        raise ValueError("len(initial_points) must be equal to num_points")
    weights = [1.0] * num_points
    if dist_matrix_function is None:
        dist_matrix_function = calc_euclidean_dist_matrix

    # begin iteration
    for _ in range(num_steps):
        if callback is not None:
            callback(cluster_centers)
        random_point = np.random.rand(1, dimension)
        distances = dist_matrix_function(random_point, cluster_centers)
        random_point = random_point.ravel()
        nearest_index = int(np.argmin(distances, axis=1))
        nearest_cluster_center = cluster_centers[nearest_index, :].ravel()
        if (
            hasattr(dist_matrix_function, "max_dists_per_dim")
            and dist_matrix_function.max_dists_per_dim is not None
        ):
            one_dim_dists = np.abs(nearest_cluster_center - random_point)
            virtual_point = np.array(random_point)
            for j, dist in enumerate(one_dim_dists):
                if dist > 0.5:
                    if nearest_cluster_center[j] < 0.5:
                        virtual_point[j] = 1.0 - random_point[j]
                    else:
                        virtual_point[j] = 1.0 + random_point[j]
        else:
            virtual_point = random_point
        weight = weights[nearest_index]
        cluster_centers[nearest_index, :] = (
            weight * nearest_cluster_center + virtual_point
        ) / (weight + 1.0)
        cluster_centers[nearest_index, :] %= 1.0
        assert np.all(cluster_centers[nearest_index, :] <= 1.0)
        assert np.all(cluster_centers[nearest_index, :] >= 0.0)
        weights[nearest_index] += 1.0

    return cluster_centers

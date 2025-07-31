import itertools

import numpy as np


def sukharev_grid(num_points, dimension):
    """Create Sukharev grid in unit hypercube.

    Special property of this grid is that points are not placed on the
    boundaries of the hypercube, but at centroids of the `num_points`
    subcells. This design offers optimal results for the covering radius
    regarding distances based on the max-norm.

    Parameters
    ----------
    num_points : int
        The number of points to generate.
        ``num_points ** (1/dimension)`` must be integer.
    dimension : int
        The dimension of the space.

    Returns
    -------
    points : (`num_points`, `dimension`) numpy array

    """
    points_per_axis = int(num_points ** (1.0 / dimension))
    assert points_per_axis**dimension == num_points
    possible_values = [x + 0.5 for x in range(points_per_axis)]
    divisor = points_per_axis
    for i in range(points_per_axis):
        possible_values[i] /= divisor
    points = np.array(list(itertools.product(possible_values, repeat=dimension)))

    return points

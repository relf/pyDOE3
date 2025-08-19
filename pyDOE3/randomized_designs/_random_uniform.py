import numpy as np

__all__ = ["random_uniform"]


def random_uniform(num_points, dimension):
    """
    Generate random samples from a uniform distribution over [0, 1).

    This function is a wrapper around `numpy.random.rand` and returns
    an array of shape `(num_points, dimension)` where each entry is drawn
    from a uniform distribution on the half-open interval [0.0, 1.0).

    Parameters
    ----------
    num_points : int
        Number of random points to generate (number of rows in the output array).

    dimension : int
        Dimensionality of each random point (number of columns in the output array).

    Returns
    -------
    ndarray
        An array of shape `(num_points, dimension)` containing random samples
        from a uniform distribution over [0, 1).
    """
    return np.random.rand(num_points, dimension)

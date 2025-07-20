import numpy as np
from scipy.stats.qmc import scale


def morris_sampling(
    problem: dict, N: int, num_levels: int = 4, seed: int = None
) -> np.ndarray:
    """
    Generate samples using the Morris Method (Vanilla, no optimization).

    Parameters
    ----------
    problem : dict
        Dictionary with keys:
            - 'num_vars': number of variables
            - 'names': list of variable names
            - 'bounds': list of (min, max) pairs for each variable
    N : int
        Number of trajectories to generate
    num_levels : int
        Number of levels in the grid (must be even)
    seed : int, optional
        Random seed for reproducibility

    Returns
    -------
    samples : ndarray
        Matrix of shape (N * (D+1), D) with Morris samples
    """
    if num_levels % 2 != 0:
        raise ValueError("num_levels must be an even number")

    rng = np.random.default_rng(seed)
    D = problem["num_vars"]
    bounds = np.array(problem["bounds"])

    delta = num_levels / (2 * (num_levels - 1))
    G = np.linspace(0, 1 - delta, num_levels // 2)

    samples = []

    for _ in range(N):
        # Starting point x* on the grid
        x_star = rng.choice(G, size=D)

        # Diagonal matrix of directions (+1 or -1)
        D_star = np.diag(rng.choice([-1, 1], size=D))

        # Lower-triangular B matrix
        B = np.tril(np.ones((D + 1, D), dtype=int), -1)

        # Random permutation matrix P*
        P_star = np.eye(D)
        rng.shuffle(P_star)

        # J: ones matrix
        J = np.ones((D + 1, D))

        # Construct B* (trajectory matrix)
        B_star = x_star + delta / 2 * ((2 * B @ P_star - J) @ D_star + J)

        samples.append(B_star)

    samples = np.vstack(samples)

    # Scale to problem bounds
    samples = scale(samples, bounds[:, 0], bounds[:, 1])

    return samples

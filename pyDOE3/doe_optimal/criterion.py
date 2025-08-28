"""
Optimal Experimental Design (OED)
=================================

This module implements optimality criteria for experimental design,
as used in the field of optimal experimental design (OED).

Optimal experimental designs are a class of experimental designs that
are optimal with respect to some statistical criterion, typically related
to the information matrix of the model. The goal is to estimate model parameters
with minimum variance and/or maximum information, often reducing the number of
experimental runs required for a given precision.

Key optimality criteria implemented here (see Wikipedia: https://en.wikipedia.org/wiki/Optimal_experimental_design):

- **D-optimality**: Maximizes $$|X'X|$$, giving the most information in parameters.
- **A-optimality**: Minimizes $$\trace((X'X)^{-1})$$, reducing average parameter variance.
- **E-optimality**: Maximizes smallest eigenvalue of $$X'X$$, improving worst-case precision.
- **G-optimality**: Minimizes maximum prediction variance, improving worst-case prediction.
- **I-optimality**: Minimizes average prediction variance over the design space.
- **V-optimality**: Minimizes average prediction variance at specified points.
- **C-optimality**: Minimizes variance of a chosen linear combination of parameters.
- **S-optimality**: Maximizes orthogonality and determinant, ensuring balanced design.
- **T-optimality**: Maximizes difference between competing models at design points.
"""

import numpy as np
from scipy.linalg import inv


def d_optimality(M):
    """
    Compute D-optimality criterion for a given information matrix.

    D-optimality maximizes the determinant of the information matrix.

    The D-optimality criterion is:

    $$\det(M)$$

    Parameters
    ----------
    M : ndarray of shape (p, p)
        Information matrix.

    Returns
    -------
    float
        Determinant of the information matrix.
    """
    return float(np.linalg.det(M))


def a_optimality(M):
    """
    Compute A-optimality criterion for a given information matrix.

    A-optimality minimizes the trace of the inverse information matrix.
    Returns the negative value for maximization.

    The A-optimality criterion is:

    $$-\operatorname{tr}(M^{-1})$$

    Parameters
    ----------
    M : ndarray of shape (p, p)
        Information matrix.

    Returns
    -------
    float
        Negative trace of the inverse information matrix.
    """
    return -float(np.trace(inv(M)))


def i_optimality(M_X, moment_matrix):
    """
    Compute I-optimality criterion for a given information matrix and moment matrix.

    I-optimality minimizes the average prediction variance over the design space.
    Returns the negative value for maximization.

    The I-optimality criterion is:

    $$-\operatorname{tr}(M_{\text{moment}} M_X^{-1})$$

    Parameters
    ----------
    M_X : ndarray of shape (p, p)
        Information matrix.
    moment_matrix : ndarray of shape (p, p)
        Moment matrix for the design space.

    Returns
    -------
    float
        Negative trace of moment_matrix @ inv(M_X).
    """
    return -float(np.trace(moment_matrix @ inv(M_X)))


def c_optimality(M, c):
    """
    Compute C-optimality criterion for a given information matrix and contrast vector.

    C-optimality minimizes the variance of a linear combination of parameters.
    Returns the negative value for maximization.

    The C-optimality criterion is:

    $$-c^T M^{-1} c$$

    Parameters
    ----------
    M : ndarray of shape (p, p)
        Information matrix.
    c : ndarray of shape (p,)
        Contrast vector.

    Returns
    -------
    float
        Negative variance of the linear combination.
    """
    return -float(c.T @ inv(M) @ c)


def e_optimality(M):
    """
    Compute E-optimality criterion for a given information matrix.

    E-optimality maximizes the smallest eigenvalue of the information matrix.

    The E-optimality criterion is:

    $$\min \operatorname{eig}(M)$$

    Parameters
    ----------
    M : ndarray of shape (p, p)
        Information matrix.

    Returns
    -------
    float
        Smallest eigenvalue of the information matrix.
    """
    return float(np.min(np.linalg.eigvalsh(M)))


def _pred_var_rows(rows, M_inv):
    # rows: array of shape (m, p); M_inv: (p, p)
    # returns vector of x M_inv x^T for each row x
    return np.einsum("ij,jk,ik->i", rows, M_inv, rows)


def g_optimality(M, candidates):
    """
    Compute G-optimality criterion for a given information matrix and candidate set.

    G-optimality minimizes the maximum prediction variance over the candidate set.
    Returns the negative value for maximization.

    The G-optimality criterion is:

    $$-\max_{x \in \text{candidates}} x^T M^{-1} x$$

    Parameters
    ----------
    M : ndarray of shape (p, p)
        Information matrix.
    candidates : ndarray of shape (N, p)
        Candidate points for prediction variance evaluation.

    Returns
    -------
    float
        Negative maximum prediction variance.
    """
    M_inv = inv(M)
    variances = _pred_var_rows(np.asarray(candidates), M_inv)
    return -float(np.max(variances))


def i_pred_variance(M, candidates):
    """
    (Aux) Average prediction variance over candidates (for diagnostics).

    Parameters
    ----------
    M : ndarray of shape (p, p)
        Information matrix.
    candidates : ndarray of shape (N, p)
        Candidate points for prediction variance evaluation.

    Returns
    -------
    float
        Average prediction variance over candidates.
    """
    M_inv = inv(M)
    variances = _pred_var_rows(np.asarray(candidates), M_inv)
    return float(np.mean(variances))


def v_optimality(M, test_points):
    """
    Compute V-optimality criterion for a given information matrix and test points.

    V-optimality minimizes the average prediction variance over specified test points.
    Returns the negative value for maximization.

    The V-optimality criterion is:

    $$-\frac{1}{m} \sum_{i=1}^m x_i^T M^{-1} x_i$$

    Parameters
    ----------
    M : ndarray of shape (p, p)
        Information matrix.
    test_points : ndarray of shape (m, p)
        Test points for prediction variance evaluation.

    Returns
    -------
    float
        Negative average prediction variance.
    """
    M_inv = inv(M)
    variances = _pred_var_rows(np.asarray(test_points), M_inv)
    return -float(np.mean(variances))


def s_optimality(M):
    """
    Compute S-optimality criterion for a given information matrix.

    S-optimality is the determinant divided by the product of column RMS values.
    Prefers orthogonal and high-determinant designs.

    The S-optimality criterion is:

    $$\frac{\det(M)}{\prod_j \sqrt{M_{jj}}}$$


    Parameters
    ----------
    M : ndarray of shape (p, p)
        Information matrix.

    Returns
    -------
    float
        S-optimality value.
    """
    col_rms = np.sqrt(np.clip(np.diag(M), 1e-15, None))
    return float(np.linalg.det(M) / np.prod(col_rms))


def t_optimality(X, model_diff_subset):
    """
    Compute T-optimality criterion for model discrimination at design points.

    T-optimality maximizes discrimination between two models at the chosen design points.

    The T-optimality criterion is:

    $$d^T P_X d$$

    where $P_X = X (X^T X)^{-1} X^T$ and $d$ is the model difference vector.

    Parameters
    ----------
    X : ndarray of shape (n_points, p)
        Design matrix.
    model_diff_subset : ndarray of shape (n_points,)
        Differences between models evaluated at the subset.

    Returns
    -------
    float
        Discrimination value.
    """
    H = X.T @ X
    H_inv = inv(H)
    P = X @ H_inv @ X.T
    d = model_diff_subset.reshape(-1, 1)
    return float((d.T @ P @ d).item())

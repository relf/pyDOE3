.. index:: Sparse Grids

.. _sparse_grids:

================================================================================
Sparse Grid Designs
================================================================================

The ``pyDOE3`` module provides sparse grid construction using **Smolyak's construction** [Smolyak1963]_ 
for generating experimental designs with hierarchical grid structures that maintain good 
space-filling properties while requiring significantly fewer points than traditional 
full grid approaches in high-dimensional spaces.

.. hint::
   All sparse grid functions are available with::

    >>> from pyDOE3 import doe_sparse_grid, sparse_grid_dimension, doe_sparse_cc, doe_sparse_chebyshev

Overview
========

This implementation is based on the MATLAB Sparse Grid Interpolation Toolbox by
Andreas Klimke [Klimke2005]_ and provides exact compatibility with MATLAB spinterp's spdim function.

Sparse grids use **Smolyak's construction** to overcome the curse of dimensionality:
while a full grid in :math:`d` dimensions with :math:`n` points per dimension requires 
:math:`n^d` total points, sparse grids require significantly fewer points.

**Grid Types:**
    - **Clenshaw-Curtis**: Nested grids based on Chebyshev polynomials (recommended)
    - **Chebyshev**: Points at Chebyshev polynomial extrema  
    - **Gauss-Patterson**: Quadrature-based points

.. index:: Sparse Grid Design

.. _doe_sparse_grid:

Sparse Grid Design (``doe_sparse_grid``)
================================================

The main function for generating sparse grid designs using Smolyak's construction.
This implementation exactly matches MATLAB spinterp's theoretical point counts.

**Syntax**::

    >>> doe_sparse_grid(n_level, n_factors, grid_type='clenshaw_curtis', bounds=None)

**Parameters**:

- ``n_level`` : int
    Sparse grid level. Higher levels provide more points and better accuracy.
    Level 0 gives a single center point, higher levels add structured points.

- ``n_factors`` : int
    Number of factors/dimensions in the design space.

- ``grid_type`` : {'clenshaw_curtis', 'chebyshev', 'gauss_patterson'}, default 'clenshaw_curtis'
    Type of 1D grid points to use:

    - ``'clenshaw_curtis'``: Nested Clenshaw-Curtis points (recommended)
    - ``'chebyshev'``: Chebyshev polynomial extrema points  
    - ``'gauss_patterson'``: Gauss-Patterson quadrature points

- ``bounds`` : array_like of shape (n_factors, 2), optional
    Bounds for each dimension. Each row should be [min, max].
    If None, uses unit hypercube [0, 1]^n_factors.

**Returns**:

- ``design`` : ndarray of shape (n_points, n_factors)
    Sparse grid design points.

**Examples**::

    >>> import numpy as np
    >>> from pyDOE3 import doe_sparse_grid

    >>> # Basic 2D sparse grid
    >>> design = doe_sparse_grid(n_level=3, n_factors=2)
    >>> print(f"Generated {len(design)} points in 2D")
    Generated 29 points in 2D

    >>> # High-dimensional sparse grid with custom bounds
    >>> bounds = np.array([[-1, 1], [0, 2], [-5, 5], [1, 10]])
    >>> design = doe_sparse_grid(n_level=4, n_factors=4, bounds=bounds)
    >>> print(f"4D design with {len(design)} points")
    4D design with 177 points

    >>> # Chebyshev sparse grid
    >>> design = doe_sparse_grid(n_level=2, n_factors=3, grid_type='chebyshev')
    >>> print(f"Chebyshev grid: {design.shape}")
    Chebyshev grid: (25, 3)

.. note::
   The point counts follow exact polynomial formulas from Schreiber (2000) that match
   MATLAB spinterp's spdim function:

   - Level 0: 1 point (center)
   - Level 1: 2*d + 1 points  
   - Level 2: 2*d² + 2*d + 1 points
   - Higher levels: polynomial growth in dimension

.. index:: Sparse Grid Dimension

.. _sparse_grid_dimension:

Sparse Grid Dimension (``sparse_grid_dimension``)
=================================================

Returns the expected number of points in a sparse grid without generating the
actual points. This is useful for planning and memory estimation.

**Syntax**::

    >>> sparse_grid_dimension(n_level, n_factors)

- ``n_level``: Sparse grid level (integer ≥ 0)
- ``n_factors``: Number of factors/dimensions (integer ≥ 1)

**Returns**: Integer number of points that would be generated

**Example**::

    >>> # Check point count before generation
    >>> point_count = sparse_grid_dimension(n_level=5, n_factors=8)
    >>> print(f"Level 5, 8D grid will have {point_count} points")

    >>> # Compare different levels
    >>> for level in range(1, 6):
    ...     count = sparse_grid_dimension(level, 4)
    ...     print(f"Level {level}: {count} points")

.. index:: Clenshaw-Curtis Grid

.. _doe_sparse_cc:

Clenshaw-Curtis Grid Design (``doe_sparse_cc``)
================================================

Convenience function for generating Clenshaw-Curtis sparse grids, which are
nested and provide good convergence properties for most applications.

**Syntax**::

    >>> doe_sparse_cc(n_level, n_factors, bounds=None)

- ``n_level``: Sparse grid level (integer ≥ 0)
- ``n_factors``: Number of factors/dimensions (integer ≥ 1)
- ``bounds``: Optional array of shape (n_factors, 2) for custom bounds

**Returns**: 2D numpy array of shape (n_points, n_factors)

**Example**::

    >>> design = doe_sparse_cc(n_level=5, n_factors=3)
    >>> print(f"CC grid shape: {design.shape}")
    CC grid shape: (581, 3)

.. index:: Chebyshev Grid

.. _doe_sparse_chebyshev:

Chebyshev Grid Design (``doe_sparse_chebyshev``)
=================================================

Convenience function for generating Chebyshev sparse grids using points at
the extrema of Chebyshev polynomials.

**Syntax**::

    >>> doe_sparse_chebyshev(n_level, n_factors, bounds=None)

- ``n_level``: Sparse grid level (integer ≥ 0)
- ``n_factors``: Number of factors/dimensions (integer ≥ 1)
- ``bounds``: Optional array of shape (n_factors, 2) for custom bounds

**Returns**: 2D numpy array of shape (n_points, n_factors)

**Example**::

    >>> # Custom bounds for each dimension
    >>> bounds = np.array([[-1, 1], [0, 2]])
    >>> design = doe_sparse_chebyshev(n_level=4, n_factors=2, bounds=bounds)
    >>> print(f"Chebyshev grid shape: {design.shape}")
    Chebyshev grid shape: (145, 2)

Mathematical Background
=======================

Smolyak's Construction
----------------------

Sparse grids are constructed using Smolyak's formula [Smolyak1963]_, which combines univariate
interpolation rules. For a multivariate function :math:`f`, the sparse grid 
interpolation operator is:

.. math::

   \mathcal{A}^d_{n} f = \sum_{|\mathbf{i}|_1 \leq n+d-1} (-1)^{n+d-1-|\mathbf{i}|_1} 
   \binom{d-1}{n+d-1-|\mathbf{i}|_1} \bigotimes_{j=1}^d \mathcal{U}^{i_j}

where :math:`\mathbf{i} = (i_1, \ldots, i_d)` is a multi-index and :math:`|\mathbf{i}|_1 = i_1 + \cdots + i_d`.

Point Count Formula
-------------------

For sparse grid level :math:`n` and dimension :math:`d`:

.. math::

   N(n,d) = \sum_{k=0}^{n} \binom{n-k+d-1}{d-1} \cdot 2^k

Grid Types
----------

- **Clenshaw-Curtis**: Nested grids based on Chebyshev polynomials (recommended)
- **Chebyshev**: Points at Chebyshev polynomial extrema
- **Gauss-Patterson**: Quadrature-based nested points

For detailed mathematical exposition, see the `SPINTERP documentation 
<https://people.sc.fsu.edu/~jburkardt/m_src/spinterp/help/whatis.html>`_.

Example Usage
=============

Generate a sparse grid design for 3 factors at level 4::

    >>> import numpy as np
    >>> from pyDOE3 import doe_sparse_grid, sparse_grid_dimension
    >>> 
    >>> # Check point count first
    >>> n_points = sparse_grid_dimension(n_level=4, n_factors=3)
    >>> print(f"Expected points: {n_points}")
    >>> 
    >>> # Generate grid with custom bounds
    >>> bounds = np.array([[-1, 1], [0, 2], [-5, 5]])
    >>> design = doe_sparse_grid(n_level=4, n_factors=3, bounds=bounds)
    >>> print(f"Generated: {design.shape}")
    Generated: (177, 3)



References
==========

.. [Genz1987] Genz, A. (1987). A package for testing multiple integration subroutines. 
    In P. Keast & G. Fairweather (Eds.), *Numerical Integration: Recent Developments, 
    Software and Applications* (pp. 337-340). Reidel. ISBN: 9027725144.

.. [Klimke2005] Klimke, A., & Wohlmuth, B. (2005). Algorithm 847: SPINTERP: Piecewise 
    multilinear hierarchical sparse grid interpolation in MATLAB. *ACM Transactions on 
    Mathematical Software*, 31(4), 561-579.

.. [Klimke2006] Klimke, A. (2006). *SPINTERP V2.1: Piecewise multilinear hierarchical 
    sparse grid interpolation in MATLAB: Documentation*.

.. [Smolyak1963] Smolyak, S. (1963). Quadrature and interpolation formulas for tensor 
    products of certain classes of functions. *Doklady Akademii Nauk SSSR*, 4, 240-243.

**Original MATLAB Documentation:**

- `SPINTERP Toolbox <https://people.sc.fsu.edu/~jburkardt/m_src/spinterp/spinterp.html>`_
- `Mathematical Details <https://people.sc.fsu.edu/~jburkardt/m_src/spinterp/help/whatis.html>`_
- `Implementation Guide <https://people.sc.fsu.edu/~jburkardt/m_src/spinterp/help/getting_started.html>`_
- `Function Reference <https://people.sc.fsu.edu/~jburkardt/m_src/spinterp/help/functions_list.html>`_

.. index:: Low-Discrepancy Sequences

.. _low_discrepancy:

================================================================================
Low-Discrepancy Sequences
================================================================================

Low-discrepancy sequences, also known as *quasi-random sequences*, are
used for sampling points in a multi-dimensional space in a way that fills
the space more uniformly than uncorrelated random points. These sequences
are particularly valuable in computer experiments, numerical integration,
global optimization, and design of experiments.

This section includes the following quasi-random designs:

- :ref:`Sukharev Grid <sukharev_grid>`

.. hint::
   All sequence functions are available with::

    >>> from pyDOE3 import *

.. index:: Sukharev Grid

.. _sukharev_grid:

Sukharev Grid (``sukharev_grid``)
=================================

The **Sukharev grid** is a deterministic low-discrepancy design that places
points at the centers of equally sized subcells in the unit hypercube.
Unlike random sampling, no points are located on the boundaries, which
minimizes the covering radius with respect to the max-norm.

**Syntax**::

    >>> sukharev_grid(num_points, dimension)

- ``num_points``: total number of points to generate. Must be an integer power of ``dimension``.
- ``dimension``: dimensionality of the space.

**Example**::

    >>> sukharev_grid(4, 2)
    array([[0.25, 0.25],
           [0.25, 0.75],
           [0.75, 0.25],
           [0.75, 0.75]])

.. note::
   The Sukharev grid is especially useful when deterministic space-filling
   coverage of the design space is desired.

.. seealso::

   - `Low-discrepancy sequences <https://en.wikipedia.org/wiki/Low-discrepancy_sequence>`_
   - `Quasi-Monte Carlo methods <https://en.wikipedia.org/wiki/Quasi-Monte_Carlo_method>`_

References
==========
- Sukharev, A. G. (1971). "Optimal strategies of the search for an extremum." 
  *USSR Computational Mathematics and Mathematical Physics*, 11(4), 119-137.
  https://doi.org/10.1016/0041-5553(71)90008-5

.. index:: Response Surface Designs, RSM

.. _response_surface:

================================================================================
Response Surface Designs
================================================================================

In this section, the following kinds of *response surface designs* will 
be described:

- :ref:`Box-Behnken <box_behnken>`
- :ref:`Central Composite <central_composite>`
- :ref:`Doehlert Design <doehlert_design>`

.. hint::
   All available designs can be accessed after a simple import statement::

    >>> from pyDOE3 import *

.. index:: Box-Behnken

.. _box_behnken:

Box-Behnken (``bbdesign``)
==========================

.. image:: http://www.itl.nist.gov/div898/handbook/pri/section3/gifs/bb.gif

Box-Behnken designs can be created using the following simple syntax::

    >>> bbdesign(n, center)

where ``n`` is the number of factors (at least 3 required) and ``center`` 
is the number of center points to include. If no inputs given to 
``center``, then a pre-determined number of points are automatically
included. 

Examples
--------

The default 3-factor Box-Behnken design::

    >>> bbdesign(3)
    array([[-1., -1.,  0.],
           [ 1., -1.,  0.],
           [-1.,  1.,  0.],
           [ 1.,  1.,  0.],
           [-1.,  0., -1.],
           [ 1.,  0., -1.],
           [-1.,  0.,  1.],
           [ 1.,  0.,  1.],
           [ 0., -1., -1.],
           [ 0.,  1., -1.],
           [ 0., -1.,  1.],
           [ 0.,  1.,  1.],
           [ 0.,  0.,  0.],
           [ 0.,  0.,  0.],
           [ 0.,  0.,  0.]])

A customized design with four factors, but only a single center point::

    >>> bbdesign(4, center=1)
    array([[-1., -1.,  0.,  0.],
           [ 1., -1.,  0.,  0.],
           [-1.,  1.,  0.,  0.],
           [ 1.,  1.,  0.,  0.],
           [-1.,  0., -1.,  0.],
           [ 1.,  0., -1.,  0.],
           [-1.,  0.,  1.,  0.],
           [ 1.,  0.,  1.,  0.],
           [-1.,  0.,  0., -1.],
           [ 1.,  0.,  0., -1.],
           [-1.,  0.,  0.,  1.],
           [ 1.,  0.,  0.,  1.],
           [ 0., -1., -1.,  0.],
           [ 0.,  1., -1.,  0.],
           [ 0., -1.,  1.,  0.],
           [ 0.,  1.,  1.,  0.],
           [ 0., -1.,  0., -1.],
           [ 0.,  1.,  0., -1.],
           [ 0., -1.,  0.,  1.],
           [ 0.,  1.,  0.,  1.],
           [ 0.,  0., -1., -1.],
           [ 0.,  0.,  1., -1.],
           [ 0.,  0., -1.,  1.],
           [ 0.,  0.,  1.,  1.],
           [ 0.,  0.,  0.,  0.]])

.. index:: Central Composite

.. _central_composite:

Central Composite (``ccdesign``)
================================

.. image:: http://www.itl.nist.gov/div898/handbook/pri/section3/gifs/fig5.gif

Central composite designs can be created and customized using the syntax::

    >>> ccdesign(n, center, alpha, face)

where 

- ``n`` is the number of factors, 

- ``center`` is a 2-tuple of center points (one for the factorial block,
  one for the star block, default (4, 4)), 

- ``alpha`` is either "orthogonal" (or "o", default) or "rotatable" 
  (or "r")
  
- ``face`` is either "circumscribed" (or "ccc", default), "inscribed"
  (or "cci"), or "faced" (or "ccf").

.. image:: http://www.itl.nist.gov/div898/handbook/pri/section3/gifs/ccd2.gif

The two optional keyword arguments ``alpha`` and ``face`` help describe
how the variance in the quadratic approximation is distributed. Please
see the `NIST`_ web pages if you are uncertain which options are suitable
for your situation.

.. note::
   - 'ccc' and 'cci' can be rotatable designs, but 'ccf' cannot.
   - If ``face`` is specified, while ``alpha`` is not, then the default
     value of ``alpha`` is 'orthogonal'.

Examples
--------

Simplest input, assuming default kwargs::

    >>> ccdesign(2)
    array([[-1.        , -1.        ],
           [ 1.        , -1.        ],
           [-1.        ,  1.        ],
           [ 1.        ,  1.        ],
           [ 0.        ,  0.        ],
           [ 0.        ,  0.        ],
           [ 0.        ,  0.        ],
           [ 0.        ,  0.        ],
           [-1.41421356,  0.        ],
           [ 1.41421356,  0.        ],
           [ 0.        , -1.41421356],
           [ 0.        ,  1.41421356],
           [ 0.        ,  0.        ],
           [ 0.        ,  0.        ],
           [ 0.        ,  0.        ],
           [ 0.        ,  0.        ]])

More customized input, say, for a set of computer experiments where there
isn't variability so we only need a single center point::

    >>> ccdesign(3, center=(0, 1), alpha='r', face='cci')
    array([[-0.59460356, -0.59460356, -0.59460356],
           [ 0.59460356, -0.59460356, -0.59460356],
           [-0.59460356,  0.59460356, -0.59460356],
           [ 0.59460356,  0.59460356, -0.59460356],
           [-0.59460356, -0.59460356,  0.59460356],
           [ 0.59460356, -0.59460356,  0.59460356],
           [-0.59460356,  0.59460356,  0.59460356],
           [ 0.59460356,  0.59460356,  0.59460356],
           [-1.        ,  0.        ,  0.        ],
           [ 1.        ,  0.        ,  0.        ],
           [ 0.        , -1.        ,  0.        ],
           [ 0.        ,  1.        ,  0.        ],
           [ 0.        ,  0.        , -1.        ],
           [ 0.        ,  0.        ,  1.        ],
           [ 0.        ,  0.        ,  0.        ]])

.. index:: Doehlert Design

.. _doehlert_design:

Doehlert Design (``doehlert_shell_design``, ``doehlert_simplex_design``)
========================================================================

An alternative and very useful design for second-order models is the **uniform shell design** proposed by Doehlert in 1970 [Doehlert1970]_.  
Doehlert designs are especially advantageous when optimizing multiple variables, requiring fewer experiments than central composite designs, while providing efficient and uniform coverage of the experimental domain.

The Doehlert design defines a **spherical experimental domain** and emphasizes **uniform space filling**. Although it is not orthogonal or rotatable, it is generally sufficient for practical applications.

For two variables, the Doehlert design consists of a center point and six points forming a regular hexagon, situated on a circle.

The total number of experiments is given by:

.. math::

   N = k^2 + k + C_0

where

- :math:`k` = number of factors (variables)
- :math:`C_0` = number of center points

Two implementations are included:

- ``doehlert_shell_design``: uses a shell-based spherical approach with optional center points.
- ``doehlert_simplex_design``: uses a simplex-based method to uniformly fill the design space.

Examples
--------

Create a Doehlert design with 3 factors and 1 center point using the shell approach::

    >>> doehlert_shell_design(3, num_center_points=1)
    array([[ 0.       ,  0.       ,  0.        ],
           [ 1.       ,  0.       ,  0.        ],
           [-0.5      ,  0.8660254,  0.        ],
           [-0.5      , -0.8660254,  0.        ],
           [ 0.8660254,  0.5      ,  0.        ],
           [ 0.8660254, -0.5      ,  0.        ],
           ... ])

Create a Doehlert design using the simplex approach for 3 factors::

    >>> doehlert_simplex_design(3)
    array([[ 0.      ,  0.       , 0.        ],
           [ 1.      ,  0.       , 0.        ],
           [ 0.      ,  0.8660254, 0.        ],
           [ 0.      ,  0.5      , 0.81649658],
           [-1.      ,  0.       , 0.        ],
           [ 0.      , -0.8660254, 0.        ],
           ... ])

.. note::
   Doehlert designs are recommended for response surface modeling when good space coverage and fewer experimental runs are desired.

.. [Doehlert1970] Doehlert, David H. 1970. “Uniform Shell Designs.” *Applied Statistics* 19 (3): 231. https://doi.org/10.2307/2346327

.. index:: Response Surface Designs Support

More Information
================

If the user needs more information about appropriate designs, please 
consult the following articles on Wikipedia:

- `Box-Behnken designs`_
- `Central composite designs`_
- `Doehlert design`_

There is also a wealth of information on the `NIST`_ website about the
various design matrices that can be created as well as detailed information
about designing/setting-up/running experiments in general.

Any questions, comments, bug-fixes, etc. can be forwarded to the `author`_.

.. _author: mailto:tisimst@gmail.com
.. _Box-Behnken designs: http://en.wikipedia.org/wiki/Box-Behnken_design
.. _Central composite designs: http://en.wikipedia.org/wiki/Central_composite_design
.. _Doehlert design: https://academic.oup.com/jrsssc/article/19/3/231/6882590
.. _NIST: http://www.itl.nist.gov/div898/handbook/pri/pri.htm
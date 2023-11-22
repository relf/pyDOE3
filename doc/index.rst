.. meta::
   :description: Design of experiments for Python
   :keywords: DOE, design of experiments, experimental design,
        optimization, statistics


=====================================================
``pyDOE3``: An experimental design package for python
=====================================================

**pyDOE3 is fork of pyDOE2 which is a fork of pyDOE.**

As for ``pyDOE2`` wrt to ``pyDOE``, ``pyDOE3`` came to life to solve 
bugs and issues that remained unsolved in ``pyDOE2``.

The ``pyDOE3`` package is designed to help the 
**scientist, engineer, statistician,** etc., to construct appropriate 
**experimental designs**.

.. hint::
   All available designs can be accessed after a simple import statement::

   >>> from pyDOE3 import *

    
Capabilities
============

The package currently includes functions for creating designs for any 
number of factors:

- :ref:`Factorial Designs <factorial>`

  #. :ref:`General Full-Factorial <general_full_factorial>` (``fullfact``)

  #. :ref:`2-Level Full-Factorial <2_level_full_factorial>` (``ff2n``)

  #. :ref:`2-Level Fractional-Factorial <fractional_factorial>` (``fracfact``)

  #. :ref:`Plackett-Burman <plackett_burman>` (``pbdesign``)

  #. :ref:`Generalized Subset Design <gsd>` (``gsd``)

- :ref:`Response-Surface Designs <response_surface>`

  #. :ref:`Box-Behnken <box_behnken>` (``bbdesign``)

  #. :ref:`Central-Composite <central_composite>` (``ccdesign``)

- :ref:`Randomized Designs <randomized>`

  #. :ref:`Latin-Hypercube <latin_hypercube>` (``lhs``)
  
Requirements
============

- NumPy
- SciPy

.. index:: installation

.. _installing this package:

Installation
============

.. code-block:: sh

   pip install --upgrade pyDOE3

or with Anaconda distribution

.. code-block:: sh

   conda install -c conda-forge pydoe3

Credits
=======

This code was originally published by the following individuals for use with
Scilab:
    
- Copyright (C) 2012 - 2013 - Michael Baudin
- Copyright (C) 2012 - Maria Christopoulou
- Copyright (C) 2010 - 2011 - INRIA - Michael Baudin
- Copyright (C) 2009 - Yann Collette
- Copyright (C) 2009 - CEA - Jean-Marc Martinez

pyDOE

- Copyright (c) 2014, Abraham D. Lee & tisimst

pyDOE2

- Copyright (c) 2018, Rickard Sjögren & Daniel Svensson

Much thanks goes to these individuals.

License
=======

This package is provided under The *BSD License* (3-Clause)

References
==========

- `Factorial designs`_
- `Plackett-Burman designs`_
- `Box-Behnken designs`_
- `Central composite designs`_
- `Latin-Hypercube designs`_

There is also a wealth of information on the `NIST`_ website about the
various design matrices that can be created as well as detailed information
about designing/setting-up/running experiments in general.

.. _Factorial designs: http://en.wikipedia.org/wiki/Factorial_experiment
.. _Box-Behnken designs: http://en.wikipedia.org/wiki/Box-Behnken_design
.. _Central composite designs: http://en.wikipedia.org/wiki/Central_composite_design
.. _Plackett-Burman designs: http://en.wikipedia.org/wiki/Plackett-Burman_design
.. _Latin-Hypercube designs: http://en.wikipedia.org/wiki/Latin_hypercube_sampling
.. _NIST: http://www.itl.nist.gov/div898/handbook/pri/pri.htm

[![Tests](https://github.com/relf/pyDOE3/actions/workflows/tests.yml/badge.svg)](https://github.com/relf/pyDOE3/actions/workflows/tests.yml)
[![Documentation](https://readthedocs.org/projects/pydoe3/badge/?version=latest)](https://pydoe3.readthedocs.io/en/latest/?badge=latest)


pyDOE3: An experimental design package for python
=====================================================

`pyDOE3` is a fork of the [`pyDOE2`](https://github.com/clicumu/pyDOE2) package 
that is designed to help the scientist, engineer, statistician, etc., to 
construct appropriate experimental designs.

This fork came to life to solve bugs and issues that remained unsolved in the
original package.


Capabilities
------------

The package currently includes functions for creating designs for any 
number of factors:

- Factorial Designs
    - General Full-Factorial (``fullfact``)
    - 2-level Full-Factorial (``ff2n``)
    - 2-level Fractional Factorial (``fracfact``)
    - Plackett-Burman (``pbdesign``)
    - Generalized Subset Designs (``gsd``)
- Response-Surface Designs 
    - Box-Behnken (``bbdesign``)
    - Central-Composite (``ccdesign``)
- Randomized Designs
    - Latin-Hypercube (``lhs``)
  
See [Documentation](https://pydoe3.readthedocs.io).

Requirements
------------

- NumPy
- SciPy


Installation
------------

```
pip install pyDOE3
```


Credits
-------

`pyDOE` original code was originally converted from code by the following 
individuals for use with Scilab:
    
- Copyright (C) 2012 - 2013 - Michael Baudin
- Copyright (C) 2012 - Maria Christopoulou
- Copyright (C) 2010 - 2011 - INRIA - Michael Baudin
- Copyright (C) 2009 - Yann Collette
- Copyright (C) 2009 - CEA - Jean-Marc Martinez

- Website: forge.scilab.org/index.php/p/scidoe/sourcetree/master/macros

`pyDOE` was converted to Python by the following individual:

- Copyright (c) 2014, Abraham D. Lee & timsimst

The following individuals forked and work on `pyDOE2`:

- Copyright (C) 2018 - Rickard Sjögren and Daniel Svensson


License
-------

This package is provided under the *BSD License* (3-clause)

References
----------

- [Factorial designs](http://en.wikipedia.org/wiki/Factorial_experiment)
- [Plackett-Burman designs](http://en.wikipedia.org/wiki/Plackett-Burman_design)
- [Box-Behnken designs](http://en.wikipedia.org/wiki/Box-Behnken_design)
- [Central composite designs](http://en.wikipedia.org/wiki/Central_composite_design)
- [Latin-Hypercube designs](http://en.wikipedia.org/wiki/Latin_hypercube_sampling)
- Surowiec, Izabella, Ludvig Vikström, Gustaf Hector, Erik Johansson,
Conny Vikström, and Johan Trygg. “Generalized Subset Designs in Analytical
Chemistry.” Analytical Chemistry 89, no. 12 (June 20, 2017): 6491–97.
https://doi.org/10.1021/acs.analchem.7b00506.

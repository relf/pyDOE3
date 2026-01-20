PyDOE3: An Experimental Design Package for Python
================================================

[![Tests](https://github.com/relf/pyDOE3/actions/workflows/tests.yml/badge.svg)](https://github.com/relf/pyDOE3/actions/workflows/tests.yml)
[![Documentation](https://readthedocs.org/projects/pydoe3/badge/?version=latest)](https://pydoe3.readthedocs.io/en/latest/?badge=latest)
[![DOI](https://zenodo.org/badge/709347557.svg)](https://zenodo.org/doi/10.5281/zenodo.10958492)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

[![Stack Overflow](https://img.shields.io/badge/stackoverflow-Ask%20questions-blue.svg)](
https://stackoverflow.com/questions/tagged/pydoe)
[![codecov](https://codecov.io/gh/relf/pydoe3/branch/master/graph/badge.svg?token=DO4KFMPNM0)](https://codecov.io/gh/relf/pydoe3)
[![License](https://img.shields.io/badge/license-BSD%203--Clause-blue.svg)](./LICENSE)

[![PyPI Downloads](https://img.shields.io/pypi/dm/pyDOE3.svg?label=PyPI%20downloads)](https://pypi.org/project/pyDOE3/)
[![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/pydoe3.svg?label=Conda%20downloads)](https://anaconda.org/conda-forge/pydoe3)
[![Python versions](https://img.shields.io/pypi/pyversions/pyDOE3.svg)](https://pypi.org/project/pyDOE3/)

PyDOE3 is a Python package for design of experiments (DOE), enabling scientists, engineers, and statisticians to efficiently construct experimental designs.

- **Documentation:** https://pydoe3.readthedocs.io/en/latest/
- **Source code:** https://github.com/relf/pyDOE3
- **Contributing:** https://pydoe3.readthedocs.io/en/latest/contributing/#open-a-pull-request
- **Bug reports:** https://github.com/relf/pyDOE3/issues


Overview
--------

The package provides extensive support for design-of-experiments (DOE) methods and is capable of creating designs for any number of factors.

It provides:

- **Factorial Designs**
  - General Full-Factorial (``fullfact``)
  - 2-level Full-Factorial (``ff2n``)
  - 2-level Fractional Factorial (``fracfact``)
  - Plackett-Burman (``pbdesign``)
  - Generalized Subset Designs (``gsd``)

- **Response-Surface Designs**
  - Box-Behnken (``bbdesign``)
  - Central-Composite (``ccdesign``)
  - Doehlert Design (``doehlert_shell_design``, ``doehlert_simplex_design``)

- **Randomized Designs**
  - Latin-Hypercube (``lhs``)
  - Random K-Means (``random_k_means``)
  - Random Uniform (``random_uniform``)

- **Low-Discrepancy Sequences**
  - Sukharev Grid (``sukharev_grid``)
  - Sobol’ Sequence (``sobol_sequence``)
  - Halton Sequence (``halton_sequence``)
  - Rank-1 Lattice Design (``rank1_lattice``)
  - Korobov Sequence (``korobov_sequence``)
  - Cranley-Patterson Randomization (``cranley_patterson_shift``)

- **Sampling Designs**
  - Morris Method (``morris_sampling``)
  - Saltelli Sampling (``saltelli_sampling``)

- **Taguchi Designs**
  - Orthogonal arrays and robust design utilities (``taguchi_design``, ``compute_snr``)

- **Optimal Designs**
  - Advanced optimal design algorithms (``optimal_design``)
  - Optimality criteria (``A``, ``C``, ``D``, ``E``, ``G``, ``I``, ``S``, ``T``, ``V``)
  - Search algorithms (``Sequential (Dykstra)``, ``Simple Exchange (Wynn-Mitchell)``, ``Fedorov``, ``Modified Fedorov``, ``DETMAX``)

- **Sparse Grid Designs**
  - Sparse Grid Design (``doe_sparse_grid``)
  - Sparse Grid Dimension (``sparse_grid_dimension``)

Installation
------------

```bash
pip install pyDOE3
```

License
-------

This package is provided under the *BSD License* (3-clause)

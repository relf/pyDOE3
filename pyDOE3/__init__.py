"""
`pyDOE` original code was originally converted from code by the following
individuals for use with Scilab:

- Copyright (C) 2012-2013, Michael Baudin
- Copyright (C) 2012, Maria Christopoulou
- Copyright (C) 2010-2011, INRIA, Michael Baudin
- Copyright (C) 2009, Yann Collette
- Copyright (C) 2009, CEA, Jean-Marc Martinez

`pyDOE` was converted to Python by the following individual:

- Copyright (c) 2014, Abraham D. Lee

The following individuals forked `pyDOE` and worked on `pyDOE2`:

- Copyright (C) 2018, Rickard Sjögren and Daniel Svensson

The following individuals forked `pyDOE2` and worked on `pyDOE3`:

- Copyright (C) 2023 - Rémi Lafage
"""

from pyDOE3.response_surface_designs import (
    bbdesign,
    ccdesign,
    doehlert_shell_design,
    doehlert_simplex_design,
)
from pyDOE3.factorial_designs import (
    fullfact,
    ff2n,
    fracfact,
    fracfact_by_res,
    fracfact_opt,
    fracfact_aliasing,
    alias_vector_indices,
    gsd,
    pbdesign,
    fold,
)
from pyDOE3.taguchi_designs import (
    taguchi_design,
    TaguchiObjective,
    compute_snr,
    list_orthogonal_arrays,
    get_orthogonal_array,
)
from pyDOE3.randomized_designs import lhs, random_uniform, random_k_means
from pyDOE3.sampling_designs import morris_sampling, saltelli_sampling
from pyDOE3.utils.var_regression_matrix import var_regression_matrix
from pyDOE3.low_discrepancy_sequences import (
    cranley_patterson_shift,
    halton_sequence,
    sobol_sequence,
    rank1_lattice,
    korobov_sequence,
)
from pyDOE3.stratified_sampling_designs import (
    stratified_sampling,
    stratify_conventional,
    stratify_generalized,
    reconstruct_strata_from_points,
)

__all__ = [
    "bbdesign",
    "ccdesign",
    "doehlert_shell_design",
    "doehlert_simplex_design",
    "fullfact",
    "ff2n",
    "fracfact",
    "fracfact_by_res",
    "fracfact_opt",
    "fracfact_aliasing",
    "alias_vector_indices",
    "gsd",
    "pbdesign",
    "fold",
    "taguchi_design",
    "TaguchiObjective",
    "compute_snr",
    "list_orthogonal_arrays",
    "get_orthogonal_array",
    "lhs",
    "random_uniform",
    "random_k_means",
    "morris_sampling",
    "saltelli_sampling",
    "var_regression_matrix",
    "cranley_patterson_shift",
    "halton_sequence",
    "sobol_sequence",
    "rank1_lattice",
    "korobov_sequence",
    "stratified_sampling",
    "stratify_conventional",
    "stratify_generalized",
    "reconstruct_strata_from_points",
]

from ._version import __version__  # pyright: ignore[reportMissingImports] # noqa

__authors__ = [
    "Michael Baudin",
    "Maria Christopoulou",
    "Yann Collette",
    "Jean-Marc Martinez",
    "Abraham D. Lee",
    "Rickard Sjögren",
    "Daniel Svensson",
    "Rémi Lafage",
    "Saud Zahir",
]

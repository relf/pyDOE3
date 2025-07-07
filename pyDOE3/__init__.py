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

from pyDOE3.doe_box_behnken import bbdesign
from pyDOE3.doe_composite import ccdesign
from pyDOE3.doe_factorial import (
    fullfact,
    ff2n,
    fracfact,
    fracfact_by_res,
    fracfact_opt,
    fracfact_aliasing,
    alias_vector_indices,
)
from pyDOE3.doe_taguchi import (
    taguchi_design,
    TaguchiObjective,
    compute_snr,
    list_orthogonal_arrays,
    get_orthogonal_array,
)
from pyDOE3.doe_lhs import lhs
from pyDOE3.doe_fold import fold
from pyDOE3.doe_plackett_burman import pbdesign
from pyDOE3.var_regression_matrix import var_regression_matrix
from pyDOE3.doe_gsd import gsd
from pyDOE3.doe_doehlert import doehlert_shell_design, doehlert_simplex_design

__all__ = [
    "bbdesign",
    "ccdesign",
    "fullfact",
    "ff2n",
    "fracfact",
    "fracfact_by_res",
    "fracfact_opt",
    "fracfact_aliasing",
    "alias_vector_indices",
    "lhs",
    "fold",
    "pbdesign",
    "var_regression_matrix",
    "gsd",
    "taguchi_design",
    "TaguchiObjective",
    "compute_snr",
    "list_orthogonal_arrays",
    "get_orthogonal_array",
    "doehlert_shell_design",
    "doehlert_simplex_design",
]

from ._version import __version__  # noqa

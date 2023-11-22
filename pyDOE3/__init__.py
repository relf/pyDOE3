"""
pyDOE original code was originally converted from code by the following
individuals for use with Scilab:

- Copyright (C) 2012 - 2013 - Michael Baudin
- Copyright (C) 2012 - Maria Christopoulou
- Copyright (C) 2010 - 2011 - INRIA - Michael Baudin
- Copyright (C) 2009 - Yann Collette
- Copyright (C) 2009 - CEA - Jean-Marc Martinez

- Website: forge.scilab.org/index.php/p/scidoe/sourcetree/master/macros

pyDOE was converted to Python by the following individual:

- Copyright (C) 2014, Abraham D. Lee

The following individuals forked pyDOE and works on `pyDOE2`:

- Copyright (C) 2018 - Rickard Sjoegren and Daniel Svensson

"""

from ._version import __version__

from pyDOE3.doe_box_behnken import *
from pyDOE3.doe_composite import *
from pyDOE3.doe_factorial import *
from pyDOE3.doe_lhs import *
from pyDOE3.doe_fold import *
from pyDOE3.doe_plackett_burman import *
from pyDOE3.var_regression_matrix import *
from pyDOE3.doe_gsd import gsd

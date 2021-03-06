import core, sims_flanagan

# For convenience, bring all core classes into the root namespace when importing *.
from core import *

__doc__ = 'PyKEP is the answer ... but what was the question?'
__all__ = ['core', 'sims_flanagan', 'orbit_plots', 'examples', 'trajopt', 'phasing']
__version__ = '1.2.0'

"""Detecting Installed Extensions"""
# Fill up the __extensions__ variable with all detected extensions
__extensions__ = {'matplotlib': False, 'mplot3d': False,'pygmo': False,'scikit-learn': False, 'scipy': False}

# First we check matplotlib and the availability of 3Dplots
try:
	from matplotlib import __version__ as matplotlib_ver
	__extensions__['matplotlib']=True

	#We detect the version and if more than 1.1.0 mplot3d is there
	mver = matplotlib_ver.split('.')
	mver = int(mver[0])*100 + int(mver[1])*10 + int(mver[2])
	if mver >= 110:
		__extensions__['mplot3d']=True
	del mver
except ImportError:
	pass

# We check if PyGMO is installed
try:
	from PyGMO import __version__ as pygmo_ver
	__extensions__['pygmo']=True
except ImportError:
	pass

# We check if scikit-learn is installed
try:
	from sklearn import __version__ as sklearn_ver
	__extensions__['scikit-learn']=True
except ImportError:
	pass

# We check if scipy is installed
try:
	from scipy import __version__ as scipy_ver
	__extensions__['scipy']=True
except ImportError:
	pass

import orbit_plots, examples, trajopt, phasing
	
__all__ += filter(lambda name: not name.startswith('_'),dir(core))

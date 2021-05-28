"""
molecool
A Python package for analyzing and visualizing molecular files. For molssi workshop. O varios comentarios que vengan al caso
"""

# Add imports here

from .atom_data import *
from .measure import calculate_distance, calculate_angle
from .molecule import build_bond_list, calculate_molecular_mass, calculate_center_of_mass
from .visualize import draw_molecule, draw_bond_histogram

import molecool.io

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions

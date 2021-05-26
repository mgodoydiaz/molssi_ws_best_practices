"""
molecool
A Python package for analyzing and visualizing molecular files. For molssi workshop. O varios comentarios que vengan al caso
"""

# Add imports here
from .functions import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions

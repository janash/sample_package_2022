"""
sample_package_2021
This is a sample repo for the MolSSI Best Practices Workshop - January 2021
"""

# Add imports here
from .functions import canvas
from .visualize import draw_molecule, bond_histogram
from .molecule import (
    calculate_center_of_mass,
    calculate_molecular_mass,
    build_bond_list,
)
from .measure import calculate_distance, calculate_angle

# Handle versioneer
from ._version import get_versions

versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]
del get_versions, versions

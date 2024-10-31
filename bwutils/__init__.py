"""Top-level package for bwutils."""

__author__ = """Rahul Ramesh Nair"""
__email__ = "rahulascents@gmail.com"
__version__ = "0.0.1"
__doc__ = (
    "A set of scripts for LCA related calculations using Brightway framework v 2.4.*."
)

import importlib.metadata

# Get the version of brightway2
try:
    brightway_version = importlib.metadata.version("brightway2")
except importlib.metadata.PackageNotFoundError:
    brightway_version = "Not installed"

__brightway_version__ = brightway_version

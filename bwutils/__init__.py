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

if brightway_version != "Not installed" and not brightway_version.startswith("2.4"):
    print(
        f"Warning: bwutils is designed for Brightway2 version 2.4.x. "
        f"Detected version {brightway_version}. You may experience compatibility issues."
    )
__brightway_version__ = brightway_version

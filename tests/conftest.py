# tests/conftest.py

import sys
import os

# This configuration ensures that the project root is included in the Python path during test execution.
# It allows test modules to import the main package ('riemannian_stats') correctly, avoiding import errors
# when running tests from the command line or continuous integration environments.

# By appending the parent directory (project root) to sys.path, we make the package discoverable
# regardless of the current working directory when pytest is invoked.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

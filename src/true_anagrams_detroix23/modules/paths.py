"""
ANAGRAMS
paths.py
Store paths constants.
"""
import pathlib
from typing import Final

# Directories
DICTIONARIES: Final[pathlib.Path] = pathlib.Path("./data/dictionaries")
RESULTS: Final[pathlib.Path] = pathlib.Path("./data/results")

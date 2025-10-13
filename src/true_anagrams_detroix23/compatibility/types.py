"""
TRUE ANAGRAMS
types.py
"""
import pathlib
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    import ui.loadings

checkWordArgs = tuple[str, set[str], int, pathlib.Path, Optional['ui.loadings.Spinner']]
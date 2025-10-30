"""
TRUE ANAGRAMS
types.py
"""
import pathlib
from typing import Union, Literal

checkWordArgs = tuple[str, set[str], int, pathlib.Path]

controlCharacter = Union[str, Literal[""]]
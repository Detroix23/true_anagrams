"""
TRUE ANAGRAMS
base.py
"""
from typing import Final

import compatibility.plateform
import compatibility.types as types

ESC: Final[str] = (
    "\033" if compatibility.plateform.OS == compatibility.plateform.Os.UNIX 
    else "\0x1b"
)

enable_colors: bool = True

class Style:
    """
    CLI colors.
    """
    ENDC: types.controlCharacter = ESC + '[0m'
    BOLD: types.controlCharacter = ESC + '[1m'
    UNDERLINE: types.controlCharacter = ESC + '[4m'
    FAIL: types.controlCharacter = ESC + '[91m'
    OKGREEN: types.controlCharacter = ESC + '[92m'
    WARNING: types.controlCharacter = ESC + '[93m'
    OKBLUE: types.controlCharacter = ESC + '[94m'
    HEADER: types.controlCharacter = ESC + '[95m'
    OKCYAN: types.controlCharacter = ESC + '[96m'
    

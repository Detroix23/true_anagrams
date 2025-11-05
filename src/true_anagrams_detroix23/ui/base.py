"""
TRUE ANAGRAMS
base.py
"""
import dataclasses
from typing import Final

import compatibility.plateform
import compatibility.types as types

ESC: Final[str] = (
    "\033" if compatibility.plateform.OS == compatibility.plateform.Os.UNIX 
    else "\033"
)

ENABLE_COLOR: bool = True

class _DefaultColors:
    """
    Define the defaults colors, using ESC.
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


@dataclasses.dataclass
class _Style:
    """
    CLI colors.
    """
    endc: types.controlCharacter = _DefaultColors.ENDC
    bold: types.controlCharacter = _DefaultColors.BOLD
    under: types.controlCharacter = _DefaultColors.UNDERLINE
    fail: types.controlCharacter = _DefaultColors.FAIL
    okgreen: types.controlCharacter = _DefaultColors.OKGREEN
    warning: types.controlCharacter = _DefaultColors.WARNING
    okblue: types.controlCharacter = _DefaultColors.OKBLUE
    header: types.controlCharacter = _DefaultColors.HEADER
    okcyan: types.controlCharacter = _DefaultColors.OKCYAN

    def disable_color(self) -> None:
        """
        Transform all color to an empty string.
        """
        self.endc = ""
        self.bold = ""
        self.under = ""
        self.fail = ""
        self.okgreen = ""
        self.warning = ""
        self.okblue = ""
        self.header = ""
        self.okcyan = ""

STYLE: _Style = _Style()

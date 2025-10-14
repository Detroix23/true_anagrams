"""
TRUE ANAGRAMS
plateform.py
"""
import os
import enum
from typing import Final

class Os(enum.Enum):
    """
    Define available OSes.
    """
    WINDOWS = 0
    UNIX = 1

# Current
OS: Final[Os] = Os.UNIX if os.name == "posix" else Os.WINDOWS

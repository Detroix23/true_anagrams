"""
TRUE ANAGRAMS
cli.py
"""
import sys
from typing import Final

ESC: Final[str] = "\033"

def move_up(times: int = 1) -> None:
    """
    Move the Terminal cursor up `times`.
    """
    sys.stdout.write(ESC + "[" + str(times) + "A")
    return

def clear_to_bottom() -> None:
    sys.stdout.write(ESC + "[J")

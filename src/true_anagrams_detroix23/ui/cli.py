"""
TRUE ANAGRAMS
cli.py
"""
import sys

import ui.base

def move_up(times: int = 1) -> None:
    """
    Move the Terminal cursor up `times`.
    """
    sys.stdout.write(ui.base.ESC + "[" + str(times) + "A")
    return

def clear_to_bottom() -> None:
    sys.stdout.write(ui.base.ESC + "[J")

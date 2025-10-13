"""
TRUE ANAGRAMS
logs.py
"""
import sys

DEBUG: bool = False

def dbg(message: str, *, end: str = "\n", flush: bool = False, prefix: str = " ! ") -> None:
    """
    Debug print.
    """
    if not DEBUG:
        return

    sys.stdout.write(prefix + message + end)
    
    if flush:
        sys.stdout.flush()

    return
    

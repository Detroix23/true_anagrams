"""
TRUE ANAGRAMS
logs.py
"""
import sys

def dbg(message: str, *, end: str = "\n", flush: bool = False, prefix: str = " ! ") -> None:
    """
    Debug print.
    """
    sys.stdout.write(prefix + message + end)
    
    if flush:
        sys.stdout.flush()
    

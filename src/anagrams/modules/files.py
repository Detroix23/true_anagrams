"""
TRUE ANAGRAMS
files.py
"""
import pathlib
from typing import TextIO, Iterable

# Constants.

# Define comment lines.
COMMENTS: set[str] = {
    "#"
}

def count_entries(file: TextIO) -> int:
    """
    Return the number of entries, 
    which are all the line not commented.
    """
    entries: int = 0
    for line in file:
        if not line:
            continue
        if line[0] in COMMENTS:
            continue
    
        entries += 1
    
    return entries

def load_into_list(file: TextIO) -> list[str]:
    """
    Create a Python native list from a TextIO.
    Watch for comments.
    """
    l: list[str] = list()
    for line in file:
        if not line:
            continue
        if line[0] in COMMENTS:
            continue

        l.append(line.rstrip())

    return l


def write_list(iterable: Iterable[str], path: pathlib.Path) -> None:
    """
    Create a file from a given `iterable`.
    """
    with open(path, "w") as file:
        file.write("# Generated from list. \n")
        for line in iterable:
            file.write(line + "\n")

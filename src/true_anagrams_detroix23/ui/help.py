"""
TRUE ANAGRAMS.
"""
import pathlib

def readme() -> None:
    """
    Prints to the console the README.md file.
    """
    name: pathlib.Path = pathlib.Path("./README.md")

    print("TRUE ANAGRAMS.")
    print("README.md")
    with open(name, "r") as file:
        for line in file:
            print(line)
    
    return

def help() -> None:
    """
    Print a short manual to use this script from the Terminal.
    """
    print("TRUE ANAGRAMS.")
    print("Help.")

    return
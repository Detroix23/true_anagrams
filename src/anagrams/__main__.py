"""
ANAGRAMS
__main__.py
"""
import sys

import modules.ui as ui

def main(args: list[str]) -> None:
    """
    Main entry point of the program. \n
    Take a list `args`, the run arguments.
    """
    # Default values
    error_args: list[str] = []
    loading_bars: bool = True
    ascii_art: bool = True
    credit_text: bool = True

    dictionary_name = "fr_no-diac_22k.txt"

    # Check args
    for arg in args:
        if arg == "--noloading":
            loading_bars = False
        elif arg == "--noascii":
            ascii_art = False
        elif arg == "--nocredit":
            credit_text = False
        elif arg in ["-c", "--nocontext"]:
            credit_text = False
            ascii_art = False
        else:
            error_args.append(arg)

    ui.main_ui(
        loading_bars,
        ascii_art,
        error_args,
        credit_text,
        dictionary_name,
    )

if __name__ == "__main__":
    args: list[str] = sys.argv
    args.pop(0)

    main(args)
    
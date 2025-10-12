"""
ANAGRAMS
__main__.py
"""
import sys
import enum

import modules.ui as ui
import debug.tests as tests
import debug.benchmark as benchmark

class RunMode(enum.Enum):
    MAIN = 0
    TEST = 1
    BENCHMARK = 2
    

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
    mode: RunMode = RunMode.MAIN
    prepare_dictionary: bool = True

    dictionary_name: str = "default"

    # Check args
    index: int = 0
    while index < len(args) - 1:
        arg: str = args[index]

        if arg == "-n":
            dictionary_name = args[index + 1]
        if arg == "--noloading":
            loading_bars = False
        elif arg == "--noascii":
            ascii_art = False
        elif arg == "--nocredit":
            credit_text = False
        elif arg in {"-c", "--nocontext"}:
            credit_text = False
            ascii_art = False
        elif arg in {"--test", "-t"}:
            mode = RunMode.TEST
        elif arg in  {"--bench", "-b"}:
            mode = RunMode.BENCHMARK
        elif arg == "--noprep":
            prepare_dictionary = False
        else:
            error_args.append(arg)

        index += 1

    if mode == RunMode.TEST:
        tests.tests()
    elif mode == RunMode.BENCHMARK:
        benchmark.benchmark()
    else:
        ui.main_ui(
            loading_bars,
            ascii_art,
            error_args,
            credit_text,
            dictionary_name,
            prepare_dictionary
        )


if __name__ == "__main__":
    args: list[str] = sys.argv
    args.pop(0)

    main(args)
    
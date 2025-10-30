"""
ANAGRAMS
__main__.py
"""
import sys

import modules.all_words as all_words
import compatibility.plateform
import compatibility.settings
import ui.base
import ui.interaction
import ui.help
import debug.tests as tests
import debug.benchmark as benchmark
import debug.logs


def main(args: list[str]) -> None:
    """
    Main entry point of the program. \n
    Take a list `args`, the run arguments.
    """
    # Default values.
    main_settings: compatibility.settings.Run = compatibility.settings.Run()

    # Check args
    print(f"Running on {compatibility.plateform.OS} - Args: {args}")
    index: int = 0
    read: bool = True
    sanitize_next: int = 0
    while index < len(args) and read:
        arg: str = args[index]

        if arg in {"-h", "--help"}:
            main_settings.mode = compatibility.settings.RunMode.HELP
            read = False

        elif arg == "-n":
            if index + 1 >= len(args):
                raise NameError(f"(X) - Argument `-n` need to be followed by a file name.")
            else:
                main_settings.dictionary_name = args[index + 1]
                sanitize_next = 2
        elif arg in {"-p", "--noprep"}:
            main_settings.prepare_dictionary = False
            
        elif arg in {"-d", "--debug"}:
            debug.logs.DEBUG = not debug.logs.DEBUG

        elif arg in {"-c", "--nocontext"}:
            main_settings.credit_text = False
            main_settings.ascii_art = False

        elif arg in {"-t", "--test"}:
            main_settings.mode = compatibility.settings.RunMode.TEST
            debug.logs.DEBUG = True

        elif arg in {"-b", "--bench"}:
            main_settings.mode = compatibility.settings.RunMode.BENCHMARK

        elif arg in {"-a", "--allwords"}:
            main_settings.mode = compatibility.settings.RunMode.ALL

        elif arg == "--nocolor":
            ui.base.ENABLE_COLOR = False
            ui.base.STYLE.disable_color()

        elif arg == "--noloading":
            main_settings.loading_bars = False

        elif arg == "--noascii":
            main_settings.ascii_art = False

        elif arg == "--nocredit":
            main_settings.credit_text = False
        
        elif arg == "--readme":
            main_settings.mode = compatibility.settings.RunMode.README
            read = False

        elif not sanitize_next > 0:
            main_settings.error_args.append(arg)

        sanitize_next -= 1
        index += 1

    if main_settings.mode == compatibility.settings.RunMode.TEST:
        tests.main()

    elif main_settings.mode == compatibility.settings.RunMode.BENCHMARK:
        benchmark.main()

    elif main_settings.mode == compatibility.settings.RunMode.HELP:
        ui.help.help()

    elif main_settings.mode == compatibility.settings.RunMode.README:
        ui.help.readme()

    elif main_settings.mode == compatibility.settings.RunMode.ALL:
        all_words.main(main_settings.dictionary_name)

    else:
        ui.interaction.main_ui(
            main_settings.loading_bars,
            main_settings.ascii_art,
            main_settings.error_args,
            main_settings.credit_text,
            main_settings.dictionary_name,
            main_settings.prepare_dictionary
        )


if __name__ == "__main__":
    # Terminal arguments.
    args: list[str] = sys.argv
    args.pop(0)

    # Main run.
    main(args)
    
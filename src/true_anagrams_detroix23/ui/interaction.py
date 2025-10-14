"""
ANAGRAMS
ui.py
"""
import sys
import pathlib

import modules.paths as paths
import modules.anagrams as anagrams
import modules.dictionaries as dictionaries
import modules.preparations as preparation
import ui.base
import ui.cli
import ui.loadings as loadings
import ui.art as art


def main_ui(
    loading_bars: bool,
    ascii_art: bool,
    error_args: list[str],
    credit_text: bool,
    dictionary_name: str,
    prepare_dictionary: bool,
) -> None:
    """
    Main function execute on run.
    """
    # Initialization.
    dictionnary_path: pathlib.Path = paths.DICTIONARIES / dictionary_name
    if not dictionnary_path.is_file():
        raise FileNotFoundError(f"(X) - Dictionary in {dictionnary_path} does not exist.\n")

    # Preparations.
    if prepare_dictionary:
        preparation_tag: str = "_prepared"
        if preparation.dictionary(dictionnary_path, dictionary_name + preparation_tag):
            dictionnary_path = paths.DICTIONARIES / (dictionary_name + preparation_tag)

    # Informations.
    dictionnary_infos: dictionaries.Infos = dictionaries.dict_info(dictionnary_path)

    # Loading animations.
    loading_combinations: loadings.Spinner | None = None
    loading_intersect: loadings.Spinner | None = None
    if loading_bars:
        loading_combinations = loadings.spinners["Wave2"].__copy__()
        loading_combinations.multiple = 15000
        loading_combinations.prefix = "Anagrams: "
        loading_combinations.more_counters("anagrams")

        loading_intersect = loadings.spinners["Wave2"].__copy__()
        loading_intersect.prefix = "Searching dict: "
        loading_intersect.multiple = 100
        loading_intersect.per_second = True


    # Main
    if ascii_art:
        print(art.TITLE)
    else:
        print("\n# True Anagrams.\n")

    if error_args:
        print(f"{ui.base.Style.FAIL}(!) - Some invalid arguments:", end=" ")
        for arg in error_args:
            print(f"`{arg}`", end=" ")
        print(f"{ui.base.Style.ENDC}")

    if credit_text:
        print(f"{ui.base.Style.HEADER}By Detroix23, 2025.{ui.base.Style.ENDC}")
        print(f"{art.TAB}https://github.com/Detroix23/TrueAnagrams")
        print(f"{art.TAB}CC-BY 4.0")
        print()
    print(f"{ui.base.Style.OKCYAN}Using dictionnary: {ui.base.Style.BOLD}{dictionnary_infos.path}{ui.base.Style.ENDC}")
    print(f"{art.TAB}Words: {dictionnary_infos.entries}")
    print(f"{art.TAB}Is sorted: {dictionnary_infos.sort}")
    print(f"{art.TAB}Word length: {dictionnary_infos.word_length}")


    if ascii_art:
        print(f"{art.BORDER3}")

    try:
        prompt: str = "- Enter a word: "

        while True:
            user_word: str = input(prompt + ui.base.Style.BOLD)
            print(ui.base.Style.ENDC, end="")
            
            ui.cli.move_up(1)
            ui.cli.clear_to_bottom()
            print(prompt + ui.base.Style.BOLD + ui.base.Style.OKCYAN + user_word + ui.base.Style.ENDC, flush=True)

            if user_word == "":
                ui.cli.move_up(1)
                ui.cli.clear_to_bottom()                
                sys.stdout.flush()

            elif user_word:
                user_anagrams: set[str] = anagrams.get_all_combinations(
                    user_word,
                    loading_animation=loading_combinations
                )
                print(f"Found {len(user_anagrams)} anagrams.")
                
                # Check all word's anagrams.
                matching_anagrams: set[str] = dictionaries.intersect(
                    user_anagrams,
                    dictionnary_infos.word_length,
                    dictionnary_path,
                    blacklist={user_word},
                    loading_animation=loading_intersect,
                )

                if matching_anagrams:
                    print(f"=> Correct anagrams {len(matching_anagrams)}/{len(user_anagrams)}:")
                    print(set_to_table(
                        matching_anagrams,
                        row_prefix="\t│",
                    ))
                else:
                    print(f"=> Correct anagrams 0/{len(user_anagrams)}:")
                    print(f"\t{ui.base.Style.FAIL}No correct anagrams!{ui.base.Style.ENDC}")

                print("")
                if loading_bars and loading_combinations is not None and loading_intersect is not None:
                    loading_combinations.reset()
                    loading_intersect.reset()

    except KeyboardInterrupt:
        print(f"\n{ui.base.Style.ENDC}{ui.base.Style.WARNING}(+) - User interrupt (Ctrl+C).{ui.base.Style.ENDC}\n")


def set_to_table(
    elements: set[str], 
    max_per_col: int = 60,
    row_prefix: str = "\t",
    row_suffix: str = "",
    spacer: str = " ",
    table_footer: str = "─",
    color: str = ui.base.Style.OKGREEN
) -> str:
    """
    Return a formatted string of row-col table.
    Counts the character number.
    """
    table: str = row_prefix
    char_count: int = 0
    for element in elements:
        char_count += len(element)
        if char_count > max_per_col and len(element) <= max_per_col:
            table += f"{row_suffix}\n{row_prefix}"
        else:
            table += f"{spacer}{color}{element}{ui.base.Style.ENDC}"

    if table_footer:
        table += f"\n{row_prefix}{table_footer * max_per_col}"

    return table


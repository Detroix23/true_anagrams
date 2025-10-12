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
import ui.loadings as loadings
import ui.art as art

ESC: str = "\033"

class Style:
    ENDC = ESC + '[0m'
    BOLD = ESC + '[1m'
    UNDERLINE = ESC + '[4m'
    FAIL = ESC + '[91m'
    OKGREEN = ESC + '[92m'
    WARNING = ESC + '[93m'
    OKBLUE = ESC + '[94m'
    HEADER = ESC + '[95m'
    OKCYAN = ESC + '[96m'


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
        preparation.dictionary(dictionnary_path, dictionary_name + preparation_tag)
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
        loading_intersect.multiple = 1000
        loading_intersect.per_second = True
        loading_intersect.more_counters("words")


    # Main
    if ascii_art:
        print(art.TITLE)
    else:
        print("\n# True Anagrams.\n")

    if error_args:
        print(f"{Style.FAIL}(!) - Some invalid arguments:", end=" ")
        for arg in error_args:
            print(f"`{arg}`", end=" ")
        print(f"{Style.ENDC}")

    if credit_text:
        print(f"{Style.HEADER}By Detroix23, 2025.{Style.ENDC}")
        print(f"{art.TAB}https://github.com/Detroix23/TrueAnagrams")
        print(f"{art.TAB}CC-BY 4.0")
        print()
    print(f"{Style.OKCYAN}Using dictionnary: {Style.BOLD}{dictionnary_infos.path}{Style.ENDC}")
    print(f"{art.TAB}Words: {dictionnary_infos.entries}")
    print(f"{art.TAB}Is sorted: {dictionnary_infos.sort}")
    print(f"{art.TAB}Word length: {dictionnary_infos.word_length}")


    if ascii_art:
        print(f"{art.BORDER3}")

    try:
        while True:
            user_word: str = input(f"- Enter a word: {Style.BOLD}")
            print(f"{Style.ENDC}", end="")
            
            if user_word == "":
                # Move up.
                sys.stdout.write(ESC + "[1A")
                # Clear to the bottom end of the screen.
                # sys.stdout.write(ESC + "[J")

                sys.stdout.flush()

            elif user_word:
                user_anagrams: set[str] = anagrams.get_all_combinations(
                    user_word,
                    loading_animation=loading_combinations
                )
                print(f"Found {len(user_anagrams)} anagrams.")
                
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
                    print(f"\t{Style.FAIL}No correct anagrams!{Style.ENDC}")

                print("")
                if loading_bars and loading_combinations is not None and loading_intersect is not None:
                    loading_combinations.reset()
                    loading_intersect.reset()

    except KeyboardInterrupt:
        print(f"\n{Style.ENDC}{Style.WARNING}(+) - User interrupt (Ctrl+C).{Style.ENDC}\n")


def set_to_table(
    elements: set[str], 
    max_per_col: int = 60,
    row_prefix: str = "\t",
    row_suffix: str = "",
    spacer: str = " ",
    table_footer: str = "─",
    color: str = Style.OKGREEN
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
            table += f"{spacer}{color}{element}{Style.ENDC}"

    if table_footer:
        table += f"\n{row_prefix}{table_footer * max_per_col}"

    return table


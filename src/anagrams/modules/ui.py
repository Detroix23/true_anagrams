"""
ANAGRAMS
ui.py
"""

import modules.paths as paths
import modules.anagrams as anagrams
import modules.dictionnaries as dictionnaries
import modules.loadings as loadings

ART: dict[str, str] = {
    "Title": """

 _____                                                                            _____ 
( ___ )                                                                          ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |                                                                            |   | 
 |   |   ████████╗██████╗ ██╗   ██╗███████╗                                       |   | 
 |   |   ╚══██╔══╝██╔══██╗██║   ██║██╔════╝                                       |   | 
 |   |      ██║   ██████╔╝██║   ██║█████╗                                         |   | 
 |   |      ██║   ██╔══██╗██║   ██║██╔══╝                                         |   | 
 |   |      ██║   ██║  ██║╚██████╔╝███████╗                                       |   | 
 |   |      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝                                       |   | 
 |   |    █████╗ ███╗   ██╗ █████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗███████╗   |   | 
 |   |   ██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║██╔════╝   |   | 
 |   |   ███████║██╔██╗ ██║███████║██║  ███╗██████╔╝███████║██╔████╔██║███████╗   |   | 
 |   |   ██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║╚════██║   |   | 
 |   |   ██║  ██║██║ ╚████║██║  ██║╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║███████║   |   | 
 |   |   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝   |   | 
 |   |                                                                            |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                                                          (_____)
""",
    "Border1": """

     ███ ███   ███ ███   ███ ███   ███ ███   ░░░ ░░░   ░░░ ░░░     
   ███░███░  ███░███░  ███░███░  ███░███░  ███░███░  ░░░ ░░░ 
  ░░░ ░░░   ░░░ ░░░   ░░░ ░░░   ░░░ ░░░   ░░░ ░░░                   
 
"""
}

class Style:
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    FAIL = '\033[91m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    OKBLUE = '\033[94m'
    HEADER = '\033[95m'
    OKCYAN = '\033[96m'


def main_ui(
    loading_bars: bool,
    ascii_art: bool,
    error_args: list[str],
    credit_text: bool,
) -> None:
    """
    Main function execute on run.
    """
    # Vars
    dictionnary_path: paths.Path = paths.FRENCH_NO_DIAC
    
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
        loading_intersect.more_counters("words")


    # Main
    if error_args:
        print(f"{Style.FAIL}(!) - Some invalid arguments:", end=" ")
        for arg in error_args:
            print(f"`{arg}`", end=" ")
        print(f"{Style.ENDC}")

    if ascii_art:
        print(ART["Title"])
    else:
        print("\n# True Anagrams.\n")
    if credit_text:
        print(f" {Style.HEADER}By Detroix23, 2025.{Style.ENDC}")
        print("  https://github.com/Detroix23/TrueAnagrams")
        print("  CC-BY 4.0")
        print()
    print(f" {Style.OKCYAN}( Using dictionnary: {Style.BOLD}{dictionnary_path}{Style.ENDC}{Style.OKCYAN} ){Style.ENDC}")
    if ascii_art:
        print(f"{ART["Border1"]}")

    try:
        while True:
            user_word: str = input(f"- Enter a word: {Style.BOLD}")
            print(f"{Style.ENDC}", end="")
            if user_word:
                user_anagrams: set[str] = anagrams.get_all_combinations(
                    user_word,
                    loading_animation=loading_combinations
                )
                print(f"Found {len(user_anagrams)} anagrams.")
                
                matching_anagrams: set[str] = dictionnaries.intersect(
                    user_anagrams, 
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
        print(f"\n{Style.ENDC}{Style.WARNING}(+) - User interrupt (Ctrl+C).{Style.ENDC}")


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


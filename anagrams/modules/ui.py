"""
ANAGRAMS
ui.py
"""

import modules.paths as paths
import modules.anagrams as anagrams
import modules.dictionnaries as dictionnaries
import modules.loadings as loadings

def main_ui() -> None:
    """
    Main function execute on run.
    """
    # Vars
    dictionnary_path: paths.Path = paths.FRENCH_NO_DIAC
    
    # Loading animations.
    loading_intersect: loadings.Spinner = loadings.spinners["Wave2"].__copy__()
    loading_intersect.prefix = "Searching dict: "
    loading_intersect.multiple = 700
    loading_intersect.more_counters("words")
    loading_intersect.counters["words"] += 1

    loading_combinations: loadings.Spinner = loadings.spinners["Wave2"].__copy__()
    loading_combinations.multiple = 1
    loading_combinations.prefix = "Anagrams: "

    # Main
    print("# ANAGRAMS.")
    print(f"Using dictionnary: {dictionnary_path}")
    try:
        while True:
            user_word: str = input("- Enter a word: ")
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
                    loading_animation=loading_intersect
                )

                if matching_anagrams:
                    print(f"=> Correct anagrams {len(matching_anagrams)}/{len(user_anagrams)}:")
                    print(set_to_table(
                        matching_anagrams,
                        row_prefix="\t│"
                    ))
                else:
                    print(f"=> Correct anagrams 0/{len(user_anagrams)}:")
                    print("\tNo correct anagrams! ")

                print("")

    except KeyboardInterrupt:
        print("\n(+) - User interrupt (Ctrl+C).")


def set_to_table(
    elements: set[str], 
    max_per_col: int = 60,
    row_prefix: str = "\t",
    row_suffix: str = "",
    spacer: str = " ",
    table_footer: str = "─"
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
            table += f"{spacer}{element}"

    if table_footer:
        table += f"\n{row_prefix}{table_footer * max_per_col}"

    return table


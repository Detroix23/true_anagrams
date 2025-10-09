"""
ANAGRAMS
dictionnaries.py
"""
from pathlib import Path

import modules.files as files
import modules.sorting as sorting
import modules.loadings as loadings

class Infos:
    """
    A data class to nicely store informations about a natural dictionary.
    """
    entries: int
    sort: bool

    def __init__(self, entries: int, sort: bool) -> None:
        self.entries = entries
        self.sort = sort
    
    def __repr__(self) -> str:
        return f"Infos(entries: {self.entries}, sort: {self.sort})"


def dict_info(dict_path: Path) -> Infos:
    """
    Return useful info about a dictionary.
    """
    # Line count.
    entries: int = 0
    with open(dict_path, "r") as words:
        entries = files.count_entries(words)
    # Sort.
    is_sorted: bool = True

    return Infos(
        entries,
        is_sorted,
    )


def in_dict(
    word: str, 
    dictionnary_path: Path,
    loading_animation: loadings.Spinner | None = None
) -> bool:
    """
    Search using dichotomy a word.
    Parameters
    ----------
    word : str
        Word to be searched.
    dictionnary_path : Path
        Path of the dict file, sorted in alphabetic order.

    Returns
    -------
    bool
        True if in dict, False otherwise.
    """
    ignore_case: bool = True

    def in_dict_body(
        word: str, 
        dictionnary: list[str], 
        bound_start: int, 
        bound_end: int,
        loading_animation: loadings.Spinner | None = None
    ) -> bool:
        if loading_animation is not None:
            loading_animation.increment()

        if ignore_case:
            word = word.lower()

        #print(f"start: {bound_start} {dictionnary[bound_start]}, end: {bound_end} {dictionnary[bound_end]}")
        if bound_start > bound_end:
            return False
        mid: int = (bound_start + bound_end) // 2
        mid_value: str
        if ignore_case:
            mid_value = dictionnary[mid].lower()
        else:
            mid_value = dictionnary[mid]

        # Dichotomy.
        if mid_value == word:
            return True
        
        greater: str = sorting.greater_word(mid_value, word)
        #print(f"{mid_value}, {word}: {greater}")
        if greater == mid_value:
            return in_dict_body(word, dictionnary, bound_start, mid - 1, loading_animation)
        return in_dict_body(word, dictionnary, mid + 1, bound_end, loading_animation)
    
    if not word:
        return False
    
    with open(dictionnary_path, "r") as file:
        words: list[str] = files.load_into_list(file)
        result: bool = in_dict_body(word, words, 0, len(words) - 1, loading_animation)
        return result
    
def intersect(
    words: set[str], 
    dictionnary_path: Path, 
    blacklist: set[str] = set(),
    loading_animation: loadings.Spinner | None = None,
) -> set[str]:
    """
    Use the `in_dict` function on a set to filter words.
    """
    filtered: list[str] = []

    for word in words:
        if in_dict(word, dictionnary_path, loading_animation) and word not in blacklist:
            filtered.append(word)
        if loading_animation is not None:
            loading_animation.counters["words"] += 1
    
        
    if loading_animation is not None:
        loading_animation.finish()
    print("")
    return set(filtered)



if __name__ == "__main__":
    print("# DICTIONNARIES")
    
    import paths

    print("abaisse: ", in_dict("abaisse", paths.FRENCH_NO_DIAC))
    print("kqldsflkqsdjf: ", in_dict("kqldsflkqsdjf", paths.FRENCH_NO_DIAC))
    print("zebre: ", in_dict("zebre", paths.FRENCH_NO_DIAC))
    print("<EMPTY>: ", in_dict("", paths.FRENCH_NO_DIAC))
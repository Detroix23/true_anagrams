"""
ANAGRAMS
dictionnaries.py
"""
from pathlib import Path
from typing import Optional

import modules.files as files
import modules.sorting as sorting
import modules.loadings as loadings
import debug.logs as logs

class Infos:
    """
    A data class to nicely store informations about a natural dictionary.
    """
    entries: int
    sort: bool
    path: str
    word_length: int

    def __init__(self, entries: int, sort: bool, path: str, word_length: int) -> None:
        self.entries = entries
        self.sort = sort
        self.path = path
        self.word_length = word_length

    def __repr__(self) -> str:
        return f"Infos(entries: {self.entries}, sort: {self.sort})"


def dict_info(dict_path: Path) -> Infos:
    """
    Return useful info about a dictionary.
    """
    # Line count.
    lines: list[str] = list()
    with open(dict_path, "r") as words:
        lines = files.load_into_list(words)
    # Sort.
    is_sorted: bool = sorting.check(lines)

    return Infos(
        len(lines),
        is_sorted,
        str(dict_path),
        len(lines[0])
    )


def in_dict(
    word: str,
    length: int,
    dictionnary_path: Path,
    loading_animation: Optional[loadings.Spinner] = None
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
        loading_animation: Optional[loadings.Spinner] = None
    ) -> bool:
        if loading_animation is not None:
            loading_animation.increment()

        if ignore_case:
            word = word.lower()

        #print(f"start: {bound_start} {dictionnary[bound_start]}, end: {bound_end} {dictionnary[bound_end]}")
        if bound_start > bound_end:
            return False
        mid: int = (bound_start + bound_end) // 2
        mid_value: str = dictionnary[mid]
        if ignore_case:
            mid_value = dictionnary[mid].lower()
            
        logs.dbg(f"{word} {len(word)} {sorting.str_to_int(word)}, {mid_value} {len(mid_value)} {sorting.str_to_int(mid_value)}")

        # Dichotomy.
        if sorting.str_to_int(mid_value) == sorting.str_to_int(word):
            return True
        
        #print(f"{mid_value}, {word}: {greater}")
        if sorting.is_greater(mid_value, word):
            return in_dict_body(word, dictionnary, bound_start, mid - 1, loading_animation)
        else:
            return in_dict_body(word, dictionnary, mid + 1, bound_end, loading_animation)
    
    if not word:
        return False
    
    if len(word) < length:
        delta: int = length - len(word)
        word = word + "`" * delta

    with open(dictionnary_path, "r") as file:
        words: list[str] = files.load_into_list(file)
        result: bool = in_dict_body(word, words, 0, len(words) - 1, loading_animation)
        return result
    
def intersect(
    words: set[str],
    length: int,
    dictionnary_path: Path, 
    blacklist: set[str] = set(),
    loading_animation: Optional[loadings.Spinner] = None,
) -> set[str]:
    """
    Use the `in_dict` function on a set to filter words.
    """
    filtered: list[str] = []

    for word in words:
        if in_dict(word, length, dictionnary_path, loading_animation) and word not in blacklist:
            filtered.append(word)
        if loading_animation is not None:
            loading_animation.counters["words"] += 1
    
        
    if loading_animation is not None:
        loading_animation.finish()
    print("")
    return set(filtered)



if __name__ == "__main__":
    import paths
    
    print("# DICTIONNARIES")

    path: Path = paths.DICTIONARIES / "default"
    infos: Infos = dict_info(path)

    print("abaisse: ", in_dict("abaisse", infos.word_length, path))
    print("kqldsflkqsdjf: ", in_dict("kqldsflkqsdjf", infos.word_length, path))
    print("zebre: ", in_dict("zebre", infos.word_length, path))
    print("<EMPTY>: ", in_dict("", infos.word_length, path))

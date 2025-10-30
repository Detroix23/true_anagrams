"""
ANAGRAMS
dictionnaries.py
"""
import concurrent.futures
import time
from pathlib import Path
from typing import Optional

import modules.files as files
import modules.sorting as sorting
import ui.loadings as loadings
import debug.logs as logs
import compatibility.types as types

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
    word_length: int = 0
    try:
        with open(dict_path, "r") as words:
            lines = files.load_into_list(words)
            word_length = max_length(lines)
    except FileNotFoundError:
        raise FileNotFoundError(f"(X) - File on `{dict_path}` does not exists.")
    # Sort.
    is_sorted: bool = sorting.check(lines)

    return Infos(
        len(lines),
        is_sorted,
        str(dict_path),
        word_length
    )

def max_length(dictionary: list[str]) -> int:
    """
    Return the longest word of the list.
    """
    length: int = 0
    for word in dictionary:
        length = max(length, len(word))

    return length


def in_dict(
    word: str,
    length: int,
    dictionnary_path: Path,
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
    ) -> bool:
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
            return in_dict_body(word, dictionnary, bound_start, mid - 1)
        else:
            return in_dict_body(word, dictionnary, mid + 1, bound_end)
    
    if not word:
        return False
    
    # Equalize length. Crucial, between `int` comparison.
    if len(word) < length:
        delta: int = length - len(word)
        word = word + "`" * delta

    with open(dictionnary_path, "r") as file:
        words: list[str] = files.load_into_list(file)
        result: bool = in_dict_body(word, words, 0, len(words) - 1)
        return result
    
def check_word(
    word_in: str,
    blacklist: set[str],
    length: int, 
    dictionary_path: Path,
) -> Optional[str]:
        """
        Calls `in_dict` and search a given word in the multiprocessed `intersect` function.
        """
        result: Optional[str] = None

        if in_dict(word_in, length, dictionary_path) and word_in not in blacklist:
            result = word_in

        return result

def intersect_prepare_processes(arguments: types.checkWordArgs) -> Optional[str]:
    """
    Prepare a process given `arguments`. Used mapped on the executor. \r
    Aims to replace: 
    ```python
    lambda p: check_word(*p), arguments
    ```
    """
    return check_word(*arguments)


def intersect(
    words: set[str],
    length: int,
    dictionary_path: Path, 
    blacklist: set[str] = set(),
    loading_animation: Optional[loadings.Spinner] = None,
) -> set[str]:
    """
    Use the `in_dict` function on a set to filter words. \r
    Implemented with multiprocessing.   \r
    """
    filtered: list[str] = []

    time_elapsed: float = time.perf_counter()

    # Asyncronous loop.
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Create arguments for all future processes. `Word` iterate, while the other stay constant.
        arguments: list[types.checkWordArgs] = [
            (word, blacklist, length, dictionary_path) for word in words
        ]
        
        for result in executor.map(intersect_prepare_processes, arguments):
            try:
                logs.dbg(f"! {result} {type(result)}.")
                
                if loading_animation is not None:
                    # loading_animation.counters["processes"] = len(executor._processes)
                    loading_animation.increment()
                
                if result:
                    filtered.append(result)

            except Exception as exception:
                logs.dbg(f"! {exception}")


    time_elapsed = time.perf_counter() - time_elapsed

    if loading_animation is not None:
        loading_animation.finish()
    
    print("")
    print(
        f"* t(`dictionaries.intersect`) = {time_elapsed:.2f}s, w̅ = {len(words)/time_elapsed:.2f}words/ s"
    )
    return set(filtered)


def intersect_mono(
    words: set[str],
    length: int,
    dictionnary_path: Path, 
    blacklist: set[str] = set(),
    loading_animation: Optional[loadings.Spinner] = None,
) -> set[str]:
    """
    Use the `in_dict` function on a set to filter words. \r
    Uses a classic syncronous loop. \r
    """
    filtered: list[str] = []

    def call(word_in: str) -> Optional[str]:
        """
        Calls `in_dict` and search a given word.
        """
        result: Optional[str] = None

        if in_dict(word_in, length, dictionnary_path) and word_in not in blacklist:
            result = word_in

        return result

    time_elapsed: float = time.perf_counter()

    # Syncronous loop.
    for word in words:
        result: Optional[str] = call(word)
        if result:
            filtered.append(result)

    time_elapsed = time.perf_counter() - time_elapsed

    if loading_animation is not None:
        loading_animation.finish()
    
    print("")
    print(f"Time for `intersect`: {time_elapsed:.2f}s, average: {len(words)/time_elapsed:.2f}words/ s")
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

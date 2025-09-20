"""
ANAGRAMS
dictionnaries.py
"""

from pathlib import Path
import modules.loadings as loadings

ords = list[int]

def str_to_ords(word: str) -> ords:
    ascii_chars: ords = []
    for letter in word:
        ascii_chars.append(ord(letter))
    
    return ascii_chars

def ords_to_str(ascii_list: ords) -> str:
    string: str = ""
    for index in ascii_list:
        if not 0 < index < 255:
            raise ValueError(f"(X) - Non ASCII value {index}.")
        string += chr(index)
    
    return string

def greater_str(a: str, b: str) -> str:
    if ord(a) > ord(b):
        return a
    else:
        return b

def greater_word(a: str, b: str) -> str:
    return ords_to_str(greater_ords(str_to_ords(a), str_to_ords(b)))

def greater_ords(a: ords, b: ords) -> ords:
    for i_a, i_b in zip(a, b):
        if i_a > i_b:
            return a
        elif i_b > i_a:
            return b
    
    if len(a) < len(b):
        return b
    else:
        return a

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

        if mid_value == word:
            return True
        
        greater: str = greater_word(mid_value, word)
        #print(f"{mid_value}, {word}: {greater}")
        if greater == mid_value:
            return in_dict_body(word, dictionnary, bound_start, mid - 1, loading_animation)
        return in_dict_body(word, dictionnary, mid + 1, bound_end, loading_animation)
    
    if not word:
        return False
    
    with open(dictionnary_path, "r") as file:
        words: list[str] = [line.rstrip() for line in file]
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
    
    print("")
    return set(filtered)



if __name__ == "__main__":
    print("# DICTIONNARIES")
    
    import paths
    
    print(ords_to_str(greater_ords(str_to_ords("abc"), str_to_ords("aaa"))))
    print(ords_to_str(greater_ords(str_to_ords("aaa"), str_to_ords("aaa"))))
    print(ords_to_str(greater_ords(str_to_ords("aaa"), str_to_ords("abc"))))
    print(ords_to_str(greater_ords(str_to_ords("uui"), str_to_ords("uua"))))
    
    print(greater_word("apprehension", "abaisse"))

    print("abaisse: ", in_dict("abaisse", paths.FRENCH_NO_DIAC))
    print("kqldsflkqsdjf: ", in_dict("kqldsflkqsdjf", paths.FRENCH_NO_DIAC))
    print("zebre: ", in_dict("zebre", paths.FRENCH_NO_DIAC))
    print("<EMPTY>: ", in_dict("", paths.FRENCH_NO_DIAC))
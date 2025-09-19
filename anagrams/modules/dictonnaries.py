from pathlib import Path


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
    return a


def in_dict(word: str, dictionnary_path: Path) -> bool:
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
    
    def in_dict_body(
        word: ords, 
        dictionnary: list[str], 
        bound_start: int, 
        bound_end: int
    ) -> bool:
        if bound_start > bound_end:
            return False
        mid: int = (bound_start + bound_end) // 2
        if dictionnary[mid] == word:
            return True
        elif greater_word(dictionnary[mid], word):
            return in_dict_body(word, dictionnary, bound_start, mid - 1)
        return in_dict_body(word, dictionnary, mid + 1, bound_end)
    
    if not word:
        return False
    else:
        with open(dictionnary_path, "r") as file:
            words: list[str] = [line.rstrip() for line in file]
            print(words[50:])
            return in_dict_body(word, words, 0, len(words) - 1)    
    
    

if __name__ == "__main__":
    print("# DICTIONNARIES")
    
    import paths
    
    print(ords_to_str(greater_ords(str_to_ords("abc"), str_to_ords("aaa"))))
    print(ords_to_str(greater_ords(str_to_ords("aaa"), str_to_ords("aaa"))))
    print(ords_to_str(greater_ords(str_to_ords("aaa"), str_to_ords("abc"))))
    print(ords_to_str(greater_ords(str_to_ords("uui"), str_to_ords("uua"))))
    
    
    print("", in_dict("abaisse", paths.FRENCH_NO_DIAC))
    print(in_dict("kqldsflkqsdjf", paths.FRENCH_NO_DIAC))
    print(in_dict("zebre", paths.FRENCH_NO_DIAC))
    print(in_dict("", paths.FRENCH_NO_DIAC))
    
    
    
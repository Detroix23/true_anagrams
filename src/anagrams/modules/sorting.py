"""
TRUE ANAGRAMS
sorting.py
"""

# Ords is a list of ASCII int code.
ords = list[int]

def str_to_ords(word: str) -> ords:
    """
    Convert a string to a list of unicodes.
    """
    ascii_chars: ords = []
    for letter in word:
        ascii_chars.append(ord(letter))
    
    return ascii_chars

def ords_to_str(ascii_list: ords) -> str:
    """
    Convert a list of unicodes to a string.
    """
    string: str = ""
    for index in ascii_list:
        if not 0 < index < 255:
            raise ValueError(f"(X) - Non ASCII value {index}.")
        string += chr(index)
    
    return string

def greater_char(a: str, b: str) -> str:
    """
    Return the the character that comes the last in the alphabet. \r
    It uses unicodes so can be used outside the alphabet.
    """
    if len(a) != 1 or len(b) != 1:
        raise ValueError(f"(X) - `a` and `b` must be 1 length str (a={repr(a)}, b={repr(b)})")

    if ord(a) > ord(b):
        return a
    else:
        return b

def greater_word(a: str, b: str) -> str:
    """
    Return the word that comes the last in the dictionary.
    """
    return ords_to_str(
        greater_ords(
            str_to_ords(a), 
            str_to_ords(b)
        )
    )

def greater_ords(a: ords, b: ords) -> ords:
    """
    Return the unicode list that has the biggest digits. \r
        - If a `i-digit` is bigger that the other list, return the list \r
        - If all digits are the same, return the longest list \r
    """
    for i_a, i_b in zip(a, b):
        if i_a > i_b:
            return a
        elif i_b > i_a:
            return b
    
    if len(a) < len(b):
        return b
    else:
        return a



def main() -> None:
    """
    Main test entry point.
    """
    print(ords_to_str(greater_ords(str_to_ords("abc"), str_to_ords("aaa"))))
    print(ords_to_str(greater_ords(str_to_ords("aaa"), str_to_ords("aaa"))))
    print(ords_to_str(greater_ords(str_to_ords("aaa"), str_to_ords("abc"))))
    print(ords_to_str(greater_ords(str_to_ords("uui"), str_to_ords("uua"))))
    
    print(greater_word("apprehension", "abaisse"))

if __name__ == "__main__":
    main()
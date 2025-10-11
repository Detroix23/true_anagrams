"""
TRUE ANAGRAMS
sorting.py
"""
import numpy
from typing import Union

# Ords is a list of ASCII int code.
ords = numpy.ndarray

# Ignore case.
IGNORE_CASE: bool = True

# Alphabetic range
ALPHABET: set[int] = set(range(97, 123))

def str_to_ords(word: str) -> ords:
    """
    Convert a string to a list of unicodes.
    """
    ascii_chars: ords = numpy.empty(shape=len(word), dtype=numpy.int8)
    for index, letter in enumerate(word.lower() if IGNORE_CASE else word):
        ascii_chars[index] = ord(letter)
    
    return ascii_chars

def str_to_int(word: str, base: int = 27) -> int:
    """
    Use a `base` to convert a word. \r
    Return base-10 positive int. \n
    Digits: \r
        0 = Non alphabetic character.
        ! = A
        26 = Z
    """
    number: int = 0
    for index, char in enumerate(word):
        number += ((ord(char) - 96) * (base ** (len(word) - index - 1))) if 96 < ord(char) and ord(char) < 123 else 0 

    return number

def ords_to_str(ascii_list: ords) -> str:
    """
    Convert a list of unicodes to a string.
    """
    return ''.join([chr(index) for index in ascii_list])

def int_to_str(number: int, base: int = 27) -> str:
    """
    Convert a base-`base` number into a string. 
    """
    chars: list[str] = list()
    while number > 0:
        chars.insert(0, chr(number % base + 96))
        number //= base
    
    return "".join(chars)


def greater_char(a: str, b: str) -> str:
    """
    Return the the character that comes the last in the alphabet. \r
    It uses unicodes so can be used outside the alphabet.
    """
    try:
        if ord(a) > ord(b):
            return a
        else:
            return b
        
    except TypeError:
        raise TypeError(f"(X) - `a` and `b` must be 1 length str (a={repr(a)}, b={repr(b)})")

def greater_word(a: str, b: str) -> str:
    """
    Return the word that comes the last in the dictionary.
    Alias for the selected method.
    """
    return _greater_word_int(a, b)

def _greater_word_ords(a: str, b: str) -> str:  # pyright: ignore[reportUnusedFunction]
    """
    Return the word that comes the last in the dictionary.
    Using `ords`.
    """
    return ords_to_str(
        _greater_ords(
            str_to_ords(a), 
            str_to_ords(b)
        )
    )

def _greater_word_int(a: str, b: str) -> str:
    """
    Return the word that comes the last in the dictionary.
    Using `int` comparison.
    """
    if str_to_int(a) > str_to_int(b):
        return a
    else:
        return b


def _greater_ords(a: ords, b: ords) -> ords:
    """
    Return the unicode list that has the biggest digits. \r
        - If a `i-digit` is bigger that the other list, return the list \r
        - If all digits are the same, return the longest list \r
    """
    cursor: int = 0
    a_shaped: ords
    b_shaped: ords
    if a.size > b.size:
        a_shaped = numpy.resize(a, b.size)
        b_shaped = b
    elif a.size < b.size:
        a_shaped = a
        b_shaped = numpy.resize(b, a.size)
    else:
        a_shaped = a
        b_shaped = b

    for r in numpy.column_stack((a_shaped, b_shaped)):
        a_i: int = r[0] if r[0] in ALPHABET else 255
        b_i: int = r[1] if r[1] in ALPHABET else 255
        
        if a_i > b_i:
            #print(f"a: {cursor} {r[0]}, {a=}, {b=}")
            return a
        elif b_i > a_i:
            #print(f"b: {cursor} {r[0]}, {a=}, {b=}")
            return b

        cursor += 1

    if a.size < b.size:
        return b
    else:
        return a

def is_greater(a: str, b: str) -> bool:
    """
    Return True if a is after b in the dictionary.
    """
    greatest: str = greater_word(a, b)
    
    return greatest == (a.lower() if IGNORE_CASE else a)


def check(iterable: Union[list[str], tuple[str]], *, raise_on_unsorted: bool = False) -> bool:
    """
    Verify that the given `iterable` is sorted alphabetically. \r
    """
    sort: bool = True
    index: int = 0
    while sort and index < len(iterable) - 1:
        sort = is_greater(
            iterable[index + 1],
            iterable[index]
        )
        index += 1

    if not sort and raise_on_unsorted:
        raise StopIteration(f"{index}: {iterable[index - 1]} {iterable[index]}")

    return sort

def sort(iterable: list[str]) -> None:
    """
    Sort, by reference, alphabetically an `iterable`. \r
    Insertion sort starting from the end.
    """
    rank: int = len(iterable) - 1
    word: str
    while rank > 0:
        word = iterable[rank - 1]
        sub: int = 0
        while is_greater(word, iterable[rank + sub]) and rank + sub < len(iterable) - 1:
            iterable[rank + sub - 1] = iterable[rank + sub]
            sub += 1
        
        iterable[rank + sub - 1] = word
        rank -= 1

def equalize_word_length(iterable: list[str], name: str = "equalized.txt", fill: str = "`") -> None:
    """
    Write a file where all words are of the same size. \r
    Find the maximum and complete with `fill`.
    """
    # Maximum.
    maximum: int = 0
    for word in iterable:
        if len(word) > maximum:
            maximum = len(word)

    for index, word in enumerate(iterable):
        delta: int = maximum - len(word) + 1
        iterable[index] = (word + (fill * delta))

    return


def main() -> None:
    """
    Main test entry point.
    """
    print("## Comparisons (ords).")
    assert(ords_to_str(_greater_ords(str_to_ords("abc"), str_to_ords("aaa"))) == "abc")
    assert(greater_word("aaa", "aaa") == "aaa")
    assert(greater_word("aaa", "abc") == "abc")
    assert(greater_word("uui", "uua") == "uui")
    assert(greater_word("uui", "auiasdasdasd") == "uui")
    assert(greater_word("uui", "zuiasdasdasd") == "zuiasdasdasd")

    
    print(greater_word("apprehension", "abaisse"))

    print("## Str to int.")
    print(str_to_int("a"))
    print(str_to_int("b"))
    print(str_to_int("ac"))
    print(str_to_int("ad"))
    print(str_to_int("ad "))
    print(str_to_int("ad*"))
    print(str_to_int("abc"))
    print(str_to_int("abz"))

    print(int_to_str(str_to_int("ad*")))
    print(int_to_str(str_to_int("adasd*")))
    print(int_to_str(str_to_int("ad*adsaf")))
    print(int_to_str(str_to_int("zzzzzzzzzzzzzzaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbb")))
    


if __name__ == "__main__":
    main()
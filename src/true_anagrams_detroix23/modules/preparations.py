"""
TRUE ANAGRAMS.
preparations.py
Edit, sort given dictionaries.
"""
import pathlib

import debug.logs
import modules.paths as paths
import modules.files as files
import modules.sorting as sorting

# Dictionary setup.
def dictionary(dictionnary_path: pathlib.Path, name: str = "prepared") -> bool:
    """
    Setup the main used dictionary. \r
    Return if the dictionary was not sorted.
    """
    dictionnary_sort: bool
    with open(dictionnary_path, "r") as file:
        dictionary: list[str] = files.load_into_list(file)

        # Sorting
        dictionnary_sort = sorting.check(dictionary, raise_on_unsorted=False)
        if not dictionnary_sort:
            print(f"Not ready {dictionnary_path}.")

            print("* Equalizing.")
            sorting.equalize_word_length(dictionary)

            dictionary_set: set[str] = set(dictionary)
            if len(dictionary_set) != len(dictionary):
                print(f"* Removing duplicates (Δ = {len(dictionary_set) - len(dictionary)}).")
                dictionary = no_duplicates(dictionary)

            if sorting.IGNORE_CASE:
                print("* Lower casing.")
                all_lower_case(dictionary)

            print("* Sorting.")
            sorting.sort(dictionary)

            is_sorted: bool = sorting.check(dictionary, raise_on_unsorted=True)
            print("Sorted: " + str(is_sorted))

            print("* Writing.")
            files.write_list(dictionary, paths.DICTIONARIES / name)
    
    return not dictionnary_sort


def all_lower_case(iterable: list[str]) -> None:
    """
    Lower case every word by reference in an `iterable`.
    """
    index: int = 0
    while index < len(iterable) - 1:
        iterable[index] = iterable[index].lower()
        index += 1

    return 

def no_duplicates(iterable: list[str]) -> list[str]:
    """
    Return a new list without duplicates.
    """
    debug.logs.dbg("Converting to int")
    ints: list[int] = [sorting.str_to_int(word.lower()) for word in iterable]
    clean: list[str] = list()

    for code in ints:
        word: str = sorting.int_to_str(code)
        debug.logs.dbg(f"Duplicates: {word} ({code})", end="\r")
        if word not in clean:
            clean.append(word)

    return clean

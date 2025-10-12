"""
TRUE ANAGRAMS.
preparations.py
"""
import pathlib

import modules.paths as paths
import modules.files as files
import modules.sorting as sorting

# Dictionary setup.
def dictionary(dictionnary_path: pathlib.Path, name: str = "prepared") -> None:
    """
    Setup the main used dictionary.
    """
    dictionnary_sort: bool
    with open(dictionnary_path, "r") as file:
        dictionary: list[str] = files.load_into_list(file)
        
        # Word length
        sorting.equalize_word_length(dictionary)

        # Sorting
        dictionnary_sort = sorting.check(dictionary, raise_on_unsorted=False)
        if not dictionnary_sort:
            print(f"Not ready {dictionnary_path}.")

            print("REMOVING DUPLICATES.")
            dictionary = no_duplicates(dictionary)

            if sorting.IGNORE_CASE:
                print("LOWER CASING.")
                all_lower_case(dictionary)
            
            print("EQUALIZING.")
            sorting.equalize_word_length(dictionary)

            print("SORTING A NEW")
            sorting.sort(dictionary)

            is_sorted: bool = sorting.check(dictionary, raise_on_unsorted=True)
            print("Sorted: " + str(is_sorted))

            print("WRITING A NEW")
            files.write_list(dictionary, paths.DICTIONARIES / name)
    
    return


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
    ints: list[int] = [sorting.str_to_int(word.lower()) for word in iterable]
    clean: list[str] = list()

    for code in ints:
        word = sorting.int_to_str(code)
        if word not in clean:
            clean.append(word)

    return clean

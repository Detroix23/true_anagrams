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
        dictionnary_sort = sorting.check(dictionary)
        if not dictionnary_sort:
            print("Not sorted.")
            print("EQUALIZING.")
            sorting.equalize_word_length(dictionary)
            print("SORTING A NEW")
            sorting.sort(dictionary)
            sorting.check(dictionary, raise_on_unsorted=True)
            print("WRITING A NEW")
            files.write_list(dictionary, paths.DICTIONARIES / name)
    
    return

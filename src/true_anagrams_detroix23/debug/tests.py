"""
TRUE ANAGRAMS
tests.py
"""
import time

import modules.sorting as sorting
import modules.all_words as all_words

def tests_sorting() -> float:
    """
    Entry point to general test in-dev features.
    """
    print("# True Anagrams.")
    print("## TESTING.")
    
    time_elapsed: float = time.perf_counter()

    sorting.main()

    time_elapsed = time.perf_counter() - time_elapsed
    print(f"Time elapsed: {time_elapsed:.2f}")

    return time_elapsed

def test_all_words() -> None:
    dictionary_name: str = "default"
    
    success, time_elapsed = all_words.run(dictionary_name)

    print(success, time_elapsed)


def main() -> None:
    test_all_words()

if __name__ == "__main__":
    main()
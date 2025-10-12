"""
TRUE ANAGRAMS
tests.py
"""
import time

import modules.sorting as sorting

def tests() -> float:
    """
    Entry point to general test in-dev features.
    """
    print("# True Anagrams.")
    print("## TESTING.")
    
    time_elapsed: float = time.monotonic()

    sorting.main()

    time_elapsed = time.monotonic() - time_elapsed
    print(f"Time elapsed: {time_elapsed:.2f}")

    return time_elapsed


def main() -> None:
    tests()

if __name__ == "__main__":
    main()
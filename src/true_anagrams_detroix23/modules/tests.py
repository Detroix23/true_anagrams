"""
TRUE ANAGRAMS
tests.py
"""
import time

import modules.sorting as sorting

def tests() -> None:
    """
    Entry point to general test in-dev features.
    """
    print("# True Anagrams.")
    print("## TESTING.")
    
    sorting.main()


def benchmark() -> None:
    """
    Benchmark.
    """
    print("# True Anagrams.")
    print("## BENCHMARKING.")

    repetitions: int = 100000
    print(f"For {repetitions} repetitions.")

    time_int: float = time.monotonic()
    for _ in range(repetitions):
        sorting._greater_word_int("abcdefghijk", "zyx")
    
    time_int = time.monotonic() - time_int

    time_ords: float = time.monotonic()
    for _ in range(repetitions):
        sorting._greater_word_ords("abcdefghijk", "zyx")
    
    time_ords = time.monotonic() - time_ords

    print(f"Int: {time_int:.2f}s")
    print(f"Ords: {time_ords:.2f}s")






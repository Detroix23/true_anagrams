"""
TRUE ANAGRAMS
benchmark.py
"""
import time
from typing import Any, Callable

import modules.sorting as sorting

result = dict[int, list[float]]

def benchmark(functions: list[Callable[[str, str], Any]], repetitions: int) -> result:
    """
    Benchmark.
    Takes a list of `functions`, and the indice of a power of ten `repetitions`.
    """
    print("# True Anagrams.")
    print("## BENCHMARKING.")

    print(f"For {repetitions} repetitions.")

    values: tuple[str, str] = ("abcdefghj", "zyxwvusty")
    results: dict[int, list[float]] = {}

    for n in range(1, repetitions):
        iteration_times: list[float] = list()

        for function in functions:
            time_elapsed: float = time.monotonic()
            
            for _ in range(10 ** n):
                function(*values)

            time_elapsed = time.monotonic() - time_elapsed    
            iteration_times.append(time_elapsed)

        results[n] = iteration_times

    return results

def print_results(results: result) -> None:
    """
    Prints a nicely formatted benchmark result.
    """
    






def main() -> None:
    results = benchmark([sorting._greater_word_int], 100000)      # pyright: ignore[reportPrivateUsage]

if __name__ == "__main__":
    main()


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

    print("Iteration: ", end="", flush=True)
    for n in range(1, repetitions + 1):
        print(n, end=", ", flush=True)
        iteration_times: list[float] = list()

        for function in functions:
            time_elapsed: float = time.monotonic()
            
            for _ in range(10 ** n):
                function(*values)

            time_elapsed = time.monotonic() - time_elapsed    
            iteration_times.append(time_elapsed)

        results[n] = iteration_times

    print()
    return results

def print_results(results: result, joint: str = " | ") -> None:
    """
    Prints a nicely formatted benchmark result.
    """
    rounding: int = 2
    maxes: list[int] = [1 for _ in range(len(results[1]))]

    # Max.
    for line in results.values():
        for index, item in enumerate(line):
            length: int = len(str(round(item, rounding)))
            if length > maxes[index]:
                maxes[index] = length

    # Template.
    template: list[str] = []
    for key, line in results.items():
        template.append(" " + str(key))
        template.append(joint)

        for index, item in enumerate(line):
            number: str = str(round(item, rounding))
            delta: int = maxes[index] - len(number)
            
            template.append(number + (" " * delta))
            template.append(joint)
        
        template.append("\n")

    print(" n" + joint + "Functions (s) ... ")
    print("--------------------" + ("-" * len(joint)))
    print("".join(template))
    




def main() -> None:
    results = benchmark([sorting._greater_word_int], 6)      # pyright: ignore[reportPrivateUsage]
    print_results(results)

if __name__ == "__main__":
    main()


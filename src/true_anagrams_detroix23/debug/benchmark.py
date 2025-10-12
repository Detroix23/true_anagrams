"""
TRUE ANAGRAMS
benchmark.py
"""
import time

import modules.sorting as sorting

def benchmark() -> list[float]:
    """
    Benchmark.
    """
    print("# True Anagrams.")
    print("## BENCHMARKING.")

    repetitions: int = 1000000000
    print(f"For {repetitions} repetitions.")

    time_int: float = time.monotonic()
    for _ in range(repetitions):
        sorting._greater_word_int("abcdefghijk", "zyx")     # pyright: ignore[reportPrivateUsage]
    
    time_int = time.monotonic() - time_int

    time_ords: float = time.monotonic()
    for _ in range(repetitions):
        sorting._greater_word_ords("abcdefghijk", "zyx")    # pyright: ignore[reportPrivateUsage]
    
    time_ords = time.monotonic() - time_ords

    print(f"Int: {time_int:.2f}s")
    print(f"Ords: {time_ords:.2f}s")

    return [time_int, time_ords]


def main() -> None:
    benchmark()

if __name__ == "__main__":
    main()


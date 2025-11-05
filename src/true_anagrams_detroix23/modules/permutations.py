"""
ANAGRAM
permutations.py
Forecast permutations quantity.
"""
import math

def anagram_combinations_count(word: str) -> int:
    """
    Compute the number of distinct number of combinations of an anagram.
    We have q / d, 
        where q is the letter number factorial,
        and d is the product of the factorial of the number of each letter
    """
    q: int = math.factorial(len(word))
    counts: list[int] = [word.count(e) for e in set(word)]
    d: int = 1
    for count in counts:
        d *= math.factorial(count)

    return q // d


if __name__ == "__main__":
    print(f"a: {anagram_combinations_count("a")}")
    print(f"a: {anagram_combinations_count("ab")}")
    print(f"a: {anagram_combinations_count("abc")}")
    print(f"a: {anagram_combinations_count("aab")}")
    print(f"a: {anagram_combinations_count("aabbc")}")
"""
ANAGRAMS
anagrams.py
"""
import ui.loadings as loadings
from typing import Optional

def slide(anagram: str, letter: str, k: int) -> str:
    """
    Insert in `k` position the letter, in between anagram.
    """
    return anagram[:k] + letter + anagram[k:]

def get_all_combinations(word: str, loading_animation: Optional[loadings.Spinner] = None) -> set[str]:
    """
    Returns a set formed of all possible anagrams of the given word.
    No duplicate; using Python's sets.
    """
    ignore_case: bool = True
    
    if ignore_case:
        word = word.lower()

    def get_all_combinations_in(word: str, loading_animation: Optional[loadings.Spinner] = None) -> set[str]:
        """
        Actual recursive function finding anagrams. 
        """
        combinations: set[str]

        if word == '' : 
            combinations = set()
        elif len(word) == 1 :
            combinations = {word}
        else:
            combinations: set[str] = set()
            for anagram in get_all_combinations_in(word[1:], loading_animation):
                for k in range(len(word)):
                    combinations.add(slide(anagram, word[0], k))
                if loading_animation is not None:
                    loading_animation.increment(len(word))
                    
        if loading_animation is not None:
            loading_animation.counters["anagrams"] = len(combinations)
        return combinations

    result: set[str] = get_all_combinations_in(word, loading_animation)
    
    if loading_animation is not None:
        loading_animation.finish()
        print("")
    return result


if __name__ == "__main__":
    print("# Modules: Anagrams.py")
    
    print("<EMPTY>: ", get_all_combinations(""))
    print("abc: ", get_all_combinations("abc"))
    print("a: ", get_all_combinations("a"))
    print("abacd", get_all_combinations("abacd"))
    
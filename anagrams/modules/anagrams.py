"""
ANAGRAMS
anagrams.py
"""

import modules.loadings as loadings

def slide(anagram: str, letter: str, k: int) -> str:
    """
    Insert in k position the lettre, in between anagram.
    """
    return anagram[:k] + letter + anagram[k:]

def get_all_combinations(word: str, loading_animation: loadings.Spinner | None = None) -> set[str]:
    """
    Returns a set formed of all possible anagrams of the given word.
    No duplicate; using Python's sets.
    """
    ignore_case: bool = True
    
    if ignore_case:
        word = word.lower()

    def get_all_combinations_in(word: str, loading_animation: loadings.Spinner | None) -> set[str]:
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

"""
# Numpy version
def get_all_combinations(word: str) -> numpy.ndarray:
    array_type = numpy.dtypes.StringDType()
    if word == '' : 
        return numpy.empty(0, dtype=array_type)
    
    combinations: numpy.ndarray = numpy.empty(math.factorial(len(word)), dtype=array_type)
    print(f"{word}")
    combinations_in: numpy.ndarray = get_all_combinations(word[1:])
    
    # print(f"{combinations_in}, size: {bool(combinations_in.size)}")
    if combinations_in.size > 1:
        for anagram in combinations_in:
            print(f"combin: {combinations_in}")
            #print(f"{anagram}, {type(anagram)}")
            for k in range(len(word)):
                combinations = numpy.append(combinations, anagram[:k] + word[0] + anagram[k:])
    return combinations
"""

if __name__ == "__main__":
    print("# Modules: Anagrams.py")
    
    print("<EMPTY>: ", get_all_combinations(""))
    print("abc: ", get_all_combinations("abc"))
    print("a: ", get_all_combinations("a"))
    print("abacd", get_all_combinations("abacd"))
    
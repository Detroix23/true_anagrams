"""
ANAGRAMS
anagrams.py
"""

import modules.loadings as loadings

def get_all_combinations(word: str, loading_animation: loadings.Spinner | None = None) -> set[str]:
    ignore_case: bool = True
    
    if ignore_case:
        word = word.lower()

    def get_all_combinations_in(word: str, loading_animation: loadings.Spinner | None) -> set[str]:
        if loading_animation is not None:
            loading_animation.increment()
        if word == '' : 
            return set()
        elif len(word) == 1 :
            return {word}
        else:
            l: list[str] = []
            for anagram in get_all_combinations_in(word[1:], loading_animation):
                for k in range(len(word)):
                    l.append(anagram[:k] + word[0] + anagram[k:])
            return set(l)

    result: set[str] = get_all_combinations_in(word, loading_animation)
    
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
    
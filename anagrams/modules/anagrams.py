"""
ANAGRAMS
anagrams.py
"""


def get_all_combinations(word: str) -> set[str]:
    if word == '' : 
        return {}
    elif len(word) == 1 :
        return {word}
    else:
        l = []
        for anagram in get_all_combinations(word[1:]):
            for k in range(len(word)):
                l.append(anagram[:k] + word[0] + anagram[k:])
        return set(l)
    


if __name__ == "__main__":
    print("# Modules: Anagrams.py")
    
    print(get_all_combinations(""))
    print(get_all_combinations("abc"))
    print(get_all_combinations("a"))
    print(get_all_combinations("abacd"))
    
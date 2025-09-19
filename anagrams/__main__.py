"""
ANAGRAMS
__main__.py
"""

import modules.paths as paths


if __name__ == "__main__":
    with open(paths.FRENCH_NO_DIAC, "r") as all_words:
        for _ in range(50):
            print(all_words.readline(), end="")
    
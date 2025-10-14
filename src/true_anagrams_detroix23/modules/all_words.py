"""
TRUE ANAGRAMS.
"""
import time
import pathlib
from typing import TextIO, Final

import modules.dictionaries as dictionaries
import modules.anagrams as anagrams
import modules.paths as paths
import debug.logs


def write_result_line(file: TextIO, word: str, matching: set[str], indentation: int = 1) -> str:
    """
    Write in a JSON format the word's result.
    Return the line as a `str`.
    """
    line: str = f'{"t" * indentation}"{word}": [{", ".join(matching)}], \n'
    debug.logs.dbg(line)
    file.write(line)

    return line


def run(dictionary_name: str) -> tuple[bool, float]:
    """
    Run an `intersect` for all words in a given dictionary. \r
    Create a new file name `dictionary_name.all` containing all words and their anagrams. \r
    Returns a tuple with `True` if the run succefully ended and the run time. \r
    """

    dictionary_path: Final[pathlib.Path] = paths.DICTIONARIES / dictionary_name
    result_path: Final[pathlib.Path] = paths.RESULTS / (dictionary_name + ".all")

    time_elapsed: float = time.perf_counter()
    success: bool = False

    try:
        with open(dictionary_path, "r") as dictionary, open(result_path, "a") as results:
            debug.logs.dbg(f"Opened {dictionary_path} {result_path}.")
            
            informations: dictionaries.Infos = dictionaries.dict_info(dictionary_path)
            debug.logs.dbg(f"Fetched informations: {informations}")

            for index, word in enumerate(dictionary):
                if word.startswith("#"):
                    continue
                
                debug.logs.dbg(f"Word {index}: {word}.", end="")

                word_anagrams: set[str] = anagrams.get_all_combinations(word)
                debug.logs.dbg(f" - # anagrams: {len(word_anagrams)}", end="")

                word_matching: set[str] = dictionaries.intersect(
                    word_anagrams,
                    informations.word_length,
                    dictionary_path,
                    blacklist={word}
                )
                debug.logs.dbg(f" - # matching {len(word_matching)}")

                write_result_line(results, word, word_matching)
        
        success = True

    except KeyboardInterrupt:
        print(f"(!) - Keyboard interrupted. The process did not finish. Time: {time.perf_counter() - time_elapsed}s.")

    except Exception as exception:
        print(f"""(!) - Unregisterd exception happend after {time.perf_counter() - time_elapsed}s ! 
Exception: {type(exception)} {repr(exception)}.
Continuing program.
""")
    
    return (success, time.perf_counter() - time_elapsed)



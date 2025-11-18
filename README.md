# True Anagrams.

Find anagrams, and find if they exist in the dictionary.

## Dictionaries
Set your own dictionaries in the `./data/dictionaries` directory.
By default, the script comes with a `default` dictionary.
- It is French with ~22k words.
- Select a dictionary using the `-n` parameter.

## Commands.
Execute the file `./src/true_angrams_detroix23/__main__.py`.
- You will enter an interactive CLI.
To configure, type `--help` as an argument while executing the scirpt, to get help about other commands.

## Prequisites.
- Run using a Virtual Environement.
- Be sure to have a tree looking like this:
```
    .
    ├── data
    ├── src
        └── true_anagrams_detroix23
            ├── __main__.py               
            └── ...
    └── ...
```
## In-depth presentation.

The program is divided in 2 main steps.  

### 1. Finding all possible anagrams.
See in `anagrams/base.py` for: 
- Recursive combinations;  
- The `set` structure.

### 2. Filtering those who are not in the dictionary.
See in `/dictionaries/base.py` for:
- Binary search;
- Multiprocessing;

See in `modules/sorting.py` for: 
- Sorting;
- Base 27, and using Python `int` growing;

### 3. Everything else.
- Minimum documentation;
- Typing using the native library `typing`;
- Class, dataclasses used like named tuples;
- Packaging;


## Thing yet to upgrade.
- Relative importing;
- Replace binary search with Hashmaps;
- Porting to Rust;
- Externaly manage the UI (using the to-be released author's CLI library);  
  

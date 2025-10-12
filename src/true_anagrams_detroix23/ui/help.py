"""
TRUE ANAGRAMS.
"""
import pathlib

import modules.paths

ARGUMENTS: dict[str, str] = {
    "-h | --help": "Print this help message.",
    "-n [dictionary name]": f"""Allow to specify a dictionary name. 
Search automatically in {modules.paths.DICTIONARIES} (constant: modules.paths.DICTIONARIES).
Default: `default`.
""",
    "-p | --noprep": """Use the dictionary without preparing it. Preparing means:
    - Check if sorted,
    - Equalizing all words with dummy characters,
    - Removing duplicates
    - Ignoring case if True,
    - Sorting it,
    - Writing a new file.
""",
    "-d | --debug": "Print debuging informations while the script is running.",
    "-c | --nocontext": "Remove all contexts and decorations.",
    "-t | --test": "Enter in feature test mode.",
    "-b | --bench": "Enter in feature benchmark mode",
    "--noloading": "",
    "--noascii": "",
    "--nocredits": "",
    "--readme": "",
}

def readme() -> None:
    """
    Prints to the console the README.md file.
    """
    name: pathlib.Path = pathlib.Path("./README.md")

    print("TRUE ANAGRAMS.")
    print("README.md")
    with open(name, "r") as file:
        for line in file:
            print(line)
    
    print()

    return

def help() -> None:
    """
    Print a short manual to use this script from the Terminal.
    """
    separator: str = ""
    
    print("TRUE ANAGRAMS.")
    print("Help.\n")

    for arg, description in ARGUMENTS.items():
        template: list[str] = [arg]
        if description:
            template.append(description)
        else:
            template.append("No description.")
        
        print(': '.join(template))
        print(separator)

    print()

    return
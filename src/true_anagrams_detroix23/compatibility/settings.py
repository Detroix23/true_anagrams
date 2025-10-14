"""
TRUE ANAGRAMS
settings.py
"""

import enum
import dataclasses

class RunMode(enum.Enum):
    """
    Available run modes.
    """
    MAIN = 0
    TEST = 1
    BENCHMARK = 2
    HELP = 3
    README = 4


@dataclasses.dataclass
class Run:
    """
    Named tuple, holding launching configuration.
    """
    error_args: list[str] = dataclasses.field(default_factory=list[str])
    loading_bars: bool = True
    ascii_art: bool = True
    credit_text: bool = True
    mode: RunMode = RunMode.MAIN
    prepare_dictionary: bool = True
    dictionary_name: str = "default_prepared"


Run.error_args = ["a"]
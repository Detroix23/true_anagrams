"""
IN PICTURE
loadings.py
Aim: loading bars and spinners like `alive_progress`, `tqdm`,...
Utilize the \r escape operator
"""

import time
from enum import Enum

class State(Enum):
    READY = 0
    RUNNING = 1
    FINISHED = 2


class Animation:
    _i: int
    first_time: float

    state: State

    def __init__(self) -> None:
        self._i = 0
        self.first_time: float = 0

        self.state: State = State.READY


class Bar(Animation):
    def __init__(
        self, 
        progress: str, 
        max_iterations: int, 
        *, true_size: int = 0, 
        empty: str = "░", 
        borders: str = "|",
        prefix: str,
        suffix: str = " ",
    ) -> None:
        super().__init__()  

        self.max: int = max_iterations if max_iterations > 0 else 1
        
        self.progress_bar_symbol: str = progress
        self.progress_bar_empty: str = empty
        self.borders: str = borders
        self.prefix: str = prefix
        self.suffix: str = suffix
        self.true_size: int = true_size
        
    def reset(self) -> None:
        """
        Reset the counter. Run this method when using default bars.
        """
        self._i = 0
        self.first_time: float = 0
        self.state = State.READY

    def increment(self, add: int = 1) -> None:
        if self.first_time == 0:
            self.first_time = time.monotonic()
            self.state = State.RUNNING
        
        self._i += add
        bar: str
        if self.true_size > 0 and self._i <= self.max:
            true_i: int = int(self.true_size * (float(self._i) / float(self.max)))
            bar = (
                self.progress_bar_symbol * true_i
                + self.progress_bar_empty * (self.true_size - true_i)
            )
        elif self.true_size > 0 and self._i > self.max:
            bar = self.progress_bar_symbol * self.true_size 
        elif self._i <= self.max:
            bar = (
                self.progress_bar_symbol * self._i
                + self.progress_bar_empty * (self.max - self._i)
            )
        else:
            bar = self.progress_bar_symbol * self.max

        template: str = "\r"

        template += self.prefix
        template += self.borders
        template += bar
        template += self.borders
        template += " - "

        percentage: float = self._i / self.max * 100
        template += f"{percentage:.1f}% "
        template += f"{self._i}/{self.max}ops "

        time_elapsed: float = time.monotonic() - self.first_time
        template += f"{time_elapsed:.2f}s "

        template += self.suffix

        print(
            template,
            end="\r"
        )
    
    def finish(self) -> None:
        """
        Allow to prematurly and ensure the bar to complete.
        Fill the bar on call.
        """
        if self._i < self.max:
            self._i = self.max
        
        self.state = State.FINISHED
        self.increment(0)

class Spinner(Animation):
    def __init__(
        self, 
        symbols: list[str] | str, 
        max: int = 0,
        *, span: int = 1, 
        multiple: int = 1,
        finish: str = "█",
        borders: str = "|",
        prefix: str = "Loading: ",
        suffix: str = " ",
        more_counters: list[str] = list(),
        more_per_second: bool = False,
    ) -> None:
        super().__init__()

        self.max: int = max
        self.multiple: int = multiple
        
        self.symbols: list[str] | str = symbols
        self.borders: str = borders
        self.prefix: str = prefix
        self.suffix: str = suffix
        self.span: int = span
        
        self.finish_character: str = finish
        self.ready_character: str = "..."

        self.counters: dict[str, int] = {counter: 0 for counter in more_counters}
        self.per_second: bool = more_per_second

    def more_counters(self, more_counters: list[str] | str) -> None:
        """
        Define more counter, after initialization.
        """
        if isinstance(more_counters, list):
            self.counters = {counter: 0 for counter in more_counters}
        else:
            self.counters = {more_counters: 0}

    def reset(self) -> None:
        """
        Reset the counter. Run this method when using default bars.
        """
        self._i = 0
        self.first_time: float = 0
        self.state = State.READY
        # Update custom counters
        self.counters = {key: 0 for key in self.counters.keys()}

    def increment(self, add: int = 1) -> None:
        """
        Progress the bar for 1 tick.
        """
        if self.first_time == 0:
            self.first_time = time.monotonic()
            self.state = State.RUNNING
        
        self._i += add
        i: int = self._i // self.multiple
        
        spinner: str = ""
        for j in range(self.span):
            spinner += self.symbols[(i + j) % len(self.symbols)]
        
        time_elapsed: float = time.monotonic() - self.first_time

        template: str = "\r"

        # Drawing
        template += self.prefix
        template += self.borders
        if self.state == State.FINISHED:
            template += f"{self.finish_character * self.span}"
        elif self.state == State.READY:
            template += f"{self.ready_character * self.span}"
        else:
            template += spinner
        template += self.borders
        template += " - "

        # Main counter
        if self.max != 0:
            percentage: float = self._i / self.max * 100
            template += f"{percentage:.1f}% "
            template += f"{self._i}/{self.max}ops "
        else:
            template += f"{self._i}ops "

        # Custom counters
        if self.counters:
            for name, count in self.counters.items():
                template += f"{name}: {count} "
                if time_elapsed != 0 and self.per_second:
                    template += f"{count / time_elapsed:.1f}/s "

        # Time counter
        template += f"{time_elapsed:.2f}s "

        template += self.suffix

        print(
            template,
            end="\r"
        )
    
    def __copy__(self) -> 'Spinner':
        copied: 'Spinner' = Spinner(
            self.symbols, 
            self.max, 
            span=self.span, 
            multiple=self.multiple
        )
        copied.reset()
        return copied

    def finish(self) -> None:
        """
        Allow to prematurly and ensure the spinner to complete.
        Set the state to FINISHED, and update one last time.
        """
        if self._i < self.max:
            self._i = self.max

        self.state = State.FINISHED
        self.increment(0)

# Default
bars: dict[str, Bar] = {
    "SimpleFull1": Bar(
        "█",
        100,
        prefix="Loading: ",
        true_size=10    
    ),
}
spinners: dict[str, Spinner] = {
    "Bars1": Spinner(
        ["│", "╲", "─", "/"],
        max=1000,
        multiple=2,
    ),
    "Wave1": Spinner(
        ["▂", "▃", "▄", "▅", "▆", "▇", "█", "▇", "▆", "▅", "▄", "▃", "▂", "▁"],
        span=3,
        multiple=1
    ),
    "Wave2": Spinner(
        ["▂", "▄", "▆", "█", "▆", "▄", "▂", "▁"],
        span=3,
        multiple=1
    ),
    # Box-drawing chars: ▖▗▘▙▚▛▜▝▞▟
    "Solid1": Spinner(
        "▙▚▘▛▞▝▜▚▗▟▞▖"
    ),
    "Solid2": Spinner(
        "▙▌▛▔▜▐▟▁"
    ),
}


if __name__ == "__main__":
    a = bars["SimpleFull1"]
    b = spinners["Bars1"]
    a.reset()
    b.reset()

    for _ in range(200):
        a.increment()
        # b.increment()
        time.sleep(0.1)

    print()    
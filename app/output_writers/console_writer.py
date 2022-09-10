"""Console output writer implementation."""
from typing import List, Optional

from app.interfaces import Finder


class ConsoleWriter:
    """Console output writer implementation."""

    def __enter__(self):
        return self

    def __exit__(self, *_):
        """For console output there's no need to do extra work on close."""

    def write(self, input_text: str, finder: Optional[Finder], results: List[str]) -> None:
        """Write output to console."""
        if finder:
            output = f"{input_text} | {finder.__class__.__name__} | {'; '.join(results)}"
        else:
            output = f"{input_text} | OK"
        print(output)

"""Output writer declaration."""
from typing import Protocol, List

from app.interfaces import Finder


class OutputWriter(Protocol):
    """Output writer interface as a context manager."""

    def __enter__(self):
        """Enter logic of context manager."""

    def __exit__(self):
        """Exit logic in the end of the context manager."""

    def write(self, input_text: str, finder: Finder, results: List[str]) -> None:
        """Write output to source."""

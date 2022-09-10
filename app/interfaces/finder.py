"""Finder declaration."""
from typing import Protocol, List


class Finder(Protocol):
    """Finder interface."""

    def find(self, text) -> List[str]:
        """Try to find smth in the text.

        Return list of found entities or empty list.
        """

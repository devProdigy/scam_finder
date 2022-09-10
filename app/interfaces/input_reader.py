"""Input reader declaration."""
from typing import Protocol, Iterator


class InputReader(Protocol):
    """Input reader interface."""

    def read_by_one(self) -> Iterator[str]:
        """Read text input one by one."""

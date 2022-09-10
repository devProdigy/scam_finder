"""Console input reader implementation."""
from typing import Iterator


class ConsoleReader:
    """Console input reader implementation."""

    def read_by_one(self) -> Iterator[str]:
        """Read user input text from console one by one."""
        while True:
            try:
                yield input("\nPlease enter text for verification: ")
            except KeyboardInterrupt:
                return

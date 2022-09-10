"""Factory input reader implementation."""
from app.input_readers.console_reader import ConsoleReader
from app.input_readers.csv_reader import CSVReader
from app.interfaces import InputReader


class InputReaderFactory:
    """Factory for input readers."""

    @staticmethod
    def create_reader(input_type: str) -> InputReader:
        """Return input reader accordingly to input_type."""
        if input_type == "console":
            return ConsoleReader()
        elif input_type == "csv":
            return CSVReader()
        else:
            raise ValueError(f"Unknown input reader type: '{input_type}'.")

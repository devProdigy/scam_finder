"""Factory output writers implementation."""
from app.interfaces import OutputWriter
from app.output_writers.console_writer import ConsoleWriter
from app.output_writers.csv_writer import CSVWriter


class OutputWriterFactory:
    """Factory for output writers."""

    @staticmethod
    def create_writer(input_type: str) -> OutputWriter:
        """Return output writer accordingly to input_type."""
        if input_type == "console":
            return ConsoleWriter()
        elif input_type == "csv":
            return CSVWriter()
        else:
            raise ValueError(f"Unknown output reader type: '{input_type}'.")

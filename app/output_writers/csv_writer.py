"""CSV file output writer implementation."""
import csv
from datetime import datetime
from typing import List, Optional

import settings
from app.interfaces import Finder


class CSVWriter:
    """CSV file output writer implementation."""

    text_data_folder_path = settings.OUTPUT_DATA_FOLDER_PATH
    csv_type_ending = ".csv"

    def __init__(self):
        self._output_file_path = self._make_output_file_path()
        self._opened_output_file = None
        self._writer = None

    def _make_output_file_path(self) -> str:
        now = datetime.now()
        writable_now = now.strftime("%m_%d_%Y_%H_%M")

        return self.text_data_folder_path / f"output_{writable_now}{self.csv_type_ending}"

    def __enter__(self):
        self._opened_output_file = open(self._output_file_path, "w+")
        self._writer = csv.writer(self._opened_output_file)

        return self

    def __exit__(self, *_):
        self._opened_output_file.close()

    def write(self, input_text: str, finder: Optional[Finder], results: List[str]) -> None:
        """Write output to csv file."""
        if finder:
            output = [input_text, finder.__class__.__name__, '; '.join(results)]
        else:
            output = [input_text, "OK", ""]

        self._writer.writerow(output)

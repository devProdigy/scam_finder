"""CSV files reader implementation."""
import csv
import os
from typing import Iterator, List

import settings


class CSVReader:
    """CSV files reader implementation."""

    text_data_folder_path = settings.INPUT_DATA_FOLDER_PATH
    csv_type_ending = ".csv"
    first_column = 0

    def read_by_one(self) -> Iterator[str]:
        """Read text from all CSV files found in data-directory one by one.

        Reads only first column. File shouldn't have header.
        """
        csv_files: List[str] = self._get_files_from_data_dir()

        for file_path in csv_files:
            with open(file_path, "r") as file:
                csv_reader = csv.reader(file)

                for row in csv_reader:
                    yield row[self.first_column]

    def _get_files_from_data_dir(self) -> List[str]:
        csv_files: List[str] = []

        for file in os.listdir(self.text_data_folder_path):
            if file.endswith(self.csv_type_ending):
                csv_file_path = self.text_data_folder_path / file

                csv_files.append(csv_file_path)

        if not csv_files:
            raise ValueError(f"No CSV file found in {self.text_data_folder_path}")

        return csv_files

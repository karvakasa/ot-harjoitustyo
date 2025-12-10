from pathlib import Path
import os


class AsiakasHistoriaRepository:

    def __init__(self, file_path):
        """finding file path for data saving"""
        self._file_path = file_path

    def _ensure_file_exists(self):
        """self check for integrity of file path"""
        Path(self._file_path).touch()

    def write(self):
        customerfile_path = os.path.join(os.path.dirname(
            __file__), "../../", "data", "asiakas.csv")

        try:
            with open(self._file_path, "r", encoding="utf-8") as f:
                rows = f.readlines()
                last_year = -1
                for row in (rows):
                    if row.lower().startswith("vuosi:"):
                        last_year = int(row.strip().split(":")[1])

                next_year = last_year + 1
        except FileNotFoundError:
            next_year = 0

        with open(self._file_path, "a", encoding="utf-8") as historyfile, \
                open(customerfile_path, "r", encoding="utf-8") as customerfile:

            historyfile.write(f"vuosi: {next_year}\n")

            for row in customerfile:
                parts = row.strip().split(",")
                if len(parts) == 2:
                    name, value = parts
                    value = float(value)
                    historyfile.write(f"{name}, {value}\n")

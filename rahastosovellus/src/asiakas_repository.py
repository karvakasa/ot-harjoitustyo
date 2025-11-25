from pathlib import Path
from asiakas import Asiakas


class AsiakasRepository:

    def __init__(self, file_path):
        self._file_path = file_path

    def find_all(self):
        return self._read()

    def create(self, asiakas):
        asiakkaat = self.find_all()
        asiakkaat.append(asiakas)

        self._write(asiakkaat)

        return asiakas

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def _read(self):
        asiakkaat = []

        self._ensure_file_exists()

        with open(self._file_path, encoding="utf-8") as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")

                nimi = parts[1]
                maara = parts[0]

                asiakkaat.append(
                    Asiakas(maara, nimi)
                )

        return asiakkaat

    def _write(self, asiakkaat):
        self._ensure_file_exists()

        with open(self._file_path, "w", encoding="utf-8") as file:
            for asiakas in asiakkaat:

                nimi = asiakas.name
                maara = asiakas.saldo

                row = f"{nimi};{maara}"

                file.write(row+"\n")

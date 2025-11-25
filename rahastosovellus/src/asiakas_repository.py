from pathlib import Path
from asiakas import Asiakas


class AsiakasRepository:

    def __init__(self, file_path):
        self._file_path = file_path

    def find_all(self):
        return self._read()

    def create(self, henkilo):
        asiakkaat = self.find_all()

        for asiakas in asiakkaat:
            if asiakas.name == henkilo.name:
                print("Asiakas löytyy jo rahastosta")
                return henkilo

        asiakkaat.append(henkilo)

        self._write(asiakkaat)

        return henkilo

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def _read(self):
        asiakkaat = []

        self._ensure_file_exists()

        with open(self._file_path, encoding="utf-8") as file:
            for rivi in file:
                rivi = rivi.replace("\n", "")
                osa = rivi.split(",")
                
                nimi = osa[1]
                maara = osa[0]

                asiakkaat.append(
                    Asiakas(maara, nimi)
                )

        return asiakkaat
    
    def count_money(self):
        asiakkaat = self.find_all()
        saldo = 0
        for asiakas in asiakkaat:
            saldo = saldo + int(asiakas.saldo)

        
        return saldo
    
    def add_money(self, henkilo):
        asiakkaat = self.find_all()
        for asiakas in asiakkaat:
            if asiakas.name == henkilo.name:
                asiakas.saldo = int(asiakas.saldo) + henkilo.saldo
                break
        self._write(asiakkaat)

    def _write(self, asiakkaat):
        self._ensure_file_exists()

        with open(self._file_path, "w", encoding="utf-8") as file:
            for asiakas in asiakkaat:

                nimi = asiakas.name
                maara = asiakas.saldo

                row = f"{nimi},{maara}"

                file.write(row+"\n")

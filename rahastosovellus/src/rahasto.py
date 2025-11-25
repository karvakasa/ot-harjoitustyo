import os
from asiakas_repository import AsiakasRepository
from asiakas import Asiakas

dirname = os.path.dirname(__file__)

class Rahasto:
    def __init__(self, saldo):
        if saldo >= 0:
            self.saldo = saldo

    def lisaa_asiakas_rahastoon(self, name, maara):

        if maara >= 0:

            asiakas = Asiakas(name, maara)
            self.saldo = self.saldo + maara
            print(f"Asiakas {asiakas} luotu")
            asiakas = Asiakas(name=name, saldo=maara)
            asiakas_repository = AsiakasRepository(
                os.path.join(dirname, "..", "data", "asiakas.csv"))
            asiakas_repository.create(asiakas)

        else:
            print("Asiakkaan luonti epäonnistui")

    def __str__(self):
        saldo = self.saldo
        return f"rahastossa on {saldo/100} euroa"

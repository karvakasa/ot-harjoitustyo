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
            print(f"Asiakas {asiakas} luotu")

            asiakas = Asiakas(name=name, saldo=maara)
            asiakas_repository = AsiakasRepository(
                os.path.join(dirname, "..", "data", "asiakas.csv"))
            asiakas_repository.create(asiakas)

            self.lisaa_rahaston_saldoa(maara)
            
        else:
            print("Asiakkaan luonti epäonnistui")

    def lisaa_rahaston_saldoa(self, maara):
        if maara >= 0:
            self.saldo = self.saldo + maara
            print(f"rahastoon lisätty {maara/100} euroa")

    def paljonko_rahaa_rahastossa(self):
        asiakas_repository = AsiakasRepository(
                os.path.join(dirname, "..", "data", "asiakas.csv"))
        saldo = asiakas_repository.count_money()

        return saldo

    def lisaa_saldoa_asiakkaalle(self, name, maara):
        if maara >= 0:
            asiakas = Asiakas(name, maara)
            asiakasrepo = AsiakasRepository(
                os.path.join(dirname, "..", "data", "asiakas.csv"))
            asiakasrepo.add_money(asiakas)

            self.lisaa_rahaston_saldoa(maara)

        else:
            print("viallinen rahamäärä")


    def __str__(self):
        saldo = self.paljonko_rahaa_rahastossa()
        return f"rahastossa on {saldo/100} euroa"

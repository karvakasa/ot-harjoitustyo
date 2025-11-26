import os
from asiakas_repository import AsiakasRepository
from asiakas import Asiakas

dirname = os.path.dirname(__file__)

class Rahasto:
    def __init__(self, balance):
        if balance >= 0:
            self.balance = balance

    def lisaa_asiakas_rahastoon(self, name, amount):

        if amount >= 0:

            customer = Asiakas(name, amount)
            print(f"Asiakas {customer} luotu")

            customer = Asiakas(name=name, balance=amount)
            asiakas_repository = AsiakasRepository(
                os.path.join(dirname, "..", "data", "asiakas.csv"))
            asiakas_repository.create(customer)

            self.lisaa_rahaston_saldoa(amount)
            
        else:
            print("Asiakkaan luonti epäonnistui")

    def lisaa_rahaston_saldoa(self, amount):
        if amount >= 0:
            self.balance = self.balance + amount
            print(f"rahastoon lisätty {amount/100} euroa")

    def paljonko_rahaa_rahastossa(self):
        asiakas_repository = AsiakasRepository(
                os.path.join(dirname, "..", "data", "asiakas.csv"))
        balance = asiakas_repository.count_money()

        return balance

    def lisaa_saldoa_asiakkaalle(self, name, amount):
        if amount >= 0:
            customer = Asiakas(name, amount)
            asiakasrepo = AsiakasRepository(
                os.path.join(dirname, "..", "data", "asiakas.csv"))
            asiakasrepo.add_money(customer)

            self.lisaa_rahaston_saldoa(amount)

        else:
            print("viallinen rahamäärä")


    def __str__(self):
        balance = self.paljonko_rahaa_rahastossa()
        return f"rahastossa on {balance/100} euroa"

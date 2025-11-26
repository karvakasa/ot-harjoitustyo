import os
from asiakas_repository import AsiakasRepository
from asiakas import Asiakas

dirname = os.path.dirname(__file__)


class Rahasto:
    def __init__(self, balance):
        if balance >= 0:
            self.balance = balance
            self.customerRepo = AsiakasRepository(
                os.path.join(dirname, "..", "data", "asiakas.csv"))

        else:
            print("viallinen rahamäärä")

    def lisaa_asiakas_rahastoon(self, name, amount):

        if amount >= 0:

            customer = Asiakas(name, amount)
            print(f"Asiakas {customer} luotu")

            customer = Asiakas(name=name, balance=amount)
            self.customerRepo.create(customer)

            self.lisaa_rahaston_saldoa(amount)

        else:
            print("viallinen rahamäärä")

    def maksa_asiakkaalle_rahaa(self, name, amount):

        if amount >= 0:
            self.customerRepo.pay_money(name, amount)

            print(f"rahat on siirretty {name}")

    def maksa_asiakkaalle_kaikki(self, name):
        customer = self.customerRepo.pay_all_money(name=name)

        print(
            f"asiakkaalle {name}, on maksettu kaikki {int(customer.balance)/100} euroa")

    def lisaa_rahaston_saldoa(self, amount):
        if amount >= 0:
            self.balance = self.balance + amount
            print(f"rahastoon lisätty {amount/100} euroa")

        else:
            print("viallinen rahamäärä")

    def paljonko_rahaa_rahastossa(self):
        balance = self.customerRepo.count_money()

        return balance

    def lisaa_saldoa_asiakkaalle(self, name, amount):
        if amount >= 0:
            customer = Asiakas(name, amount)
            self.customerRepo.add_money(customer)

            self.lisaa_rahaston_saldoa(amount)

        else:
            print("viallinen rahamäärä")

    def __str__(self):
        balance = self.paljonko_rahaa_rahastossa()
        return f"rahastossa on {balance/100} euroa"

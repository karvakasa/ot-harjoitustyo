import os
from entities.asiakas import Asiakas
from repositories.asiakas_repository import AsiakasRepository

clientdir = os.path.dirname(__file__)
clientHistorydir = os.path.dirname(__file__)

class Rahasto:
    def __init__(self, balance):
        if balance >= 0:
            self.balance = balance
            self.customerrepo = AsiakasRepository(
                os.path.join(clientdir, "../../", "data", "asiakas.csv"))

        else:
            print("viallinen rahamäärä")


    def lisaa_asiakas_rahastoon(self, name, amount):

        if amount >= 0:
            customer = Asiakas(name=name, balance=amount)
            self.customerrepo.create(customer)
            print(f"Asiakas {customer} luotu")

            self.muuta_rahaston_saldoa(amount)

        else:
            return "viallinen rahamäärä"

        return f"asiakas: {name} lisätty rahastoon"

    def maksa_asiakkaalle_rahaa(self, name, amount):

        if amount >= 0:
            self.customerrepo.pay_money(name, amount)

            print(f"rahat on siirretty {name}")

        else:
            return "viallinen rahamäärä"

        return f"asiakkaalle {name} maksettu {amount}"

    def maksa_asiakkaalle_kaikki(self, name):
        customer = self.customerrepo.pay_all_money(name=name)
        return f"asiakkaalle {name}, on maksettu kaikki {
            float(customer.balance) / 100} euroa"

    def muuta_rahaston_saldoa(self, amount):
        if amount >= 0:
            self.balance = self.balance + amount

        else:
            return "viallinen rahamäärä"

        return f"rahastoon lisätty {amount/100} euroa"

    def paljonko_rahaa_rahastossa(self):
        balance = self.customerrepo.count_money()

        return balance

    def muuta_asiakkaan_saldo(self, name, amount):
        if amount >= 0:
            customer = Asiakas(name, amount)
            self.customerrepo.add_money(customer)

            self.muuta_rahaston_saldoa(amount)

        else:
            return "viallinen rahamäärä"

        return f"asiakkaan saldoa muutettu, +{amount}"

    def nayta_asiakkaat_ja_varat(self):
        customers = self.customerrepo.find_all()
        for customer in customers:
            print("asiakas:",customer.name,
            ", varat:",float(customer.balance) / 100, "euroa.")

    def lisaa_rahaston_omiavaroja(self, amount):
        fund = Asiakas("rahaston omat", amount)
        doesfundexist = self.customerrepo.find_customer("rahaston omat")
        if doesfundexist is None:
            self.customerrepo.create(fund)
        else:
            self.customerrepo.add_money(fund)


        return f"rahaston omia varoja lisätty: {amount}"

    def pyorita_vuosi_rahastoa(self):
        customers = self.customerrepo.find_all()
        for customer in customers:
            newbalance = float(customer.balance) * 0.07
            self.muuta_asiakkaan_saldo(customer.name, newbalance)

        self.ota_vuosimaksu()

        return "vuosi mennyt"

    def ota_vuosimaksu(self):

        fundamount = 0

        customers = self.customerrepo.find_all()
        for customer in customers:
            maksu = float(customer.balance) / 50
            fundamount = fundamount + maksu
            self.lisaa_rahaston_omiavaroja(fundamount)
            newbalance = float(customer.balance) - maksu
            self.muuta_asiakkaan_saldo(customer.name, newbalance)

        return "vuosimaksu otettu"

    def poista_rahasto(self):
        self.customerrepo.delete_fund()

        return "rahasto nollattu"

    def __str__(self):
        balance = self.paljonko_rahaa_rahastossa()
        return f"rahastossa on {balance/100} euroa"

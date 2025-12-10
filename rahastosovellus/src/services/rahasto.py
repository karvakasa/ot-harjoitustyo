import os
from entities.asiakas import Asiakas
from repositories.asiakas_repository import AsiakasRepository
from services.historia import Historia

clientdir = os.path.dirname(__file__)


class Rahasto:
    def __init__(self, balance):
        """crete balance for fund and find file from filepath
        Args: 
            balance: how much is the starting balance of fund
        """
        self.historia = Historia()
        if balance >= 0:
            self.balance = balance
            self.customerrepo = AsiakasRepository(
                os.path.join(clientdir, "../../", "data", "asiakas.csv"))

        else:
            print("viallinen rahamäärä")

    def lisaa_asiakas_rahastoon(self, name, amount):
        """adding customer to fund by name and how much he invests to fund
        Args: 
            name: customer name
            amount: how much investing
        """
        if amount >= 0:
            customer = Asiakas(name=name, balance=amount)
            self.customerrepo.create(customer)
            print(f"Asiakas {customer} luotu")

            self.muuta_rahaston_saldoa(amount)
        else:
            return "viallinen rahamäärä"

        return f"asiakas: {name} lisätty rahastoon"

    def maksa_asiakkaalle_rahaa(self, name, amount):
        """paying certain amount to customer
        Args: 
            name: to who we pay
            amount: amount we pay
        """
        if amount >= 0:
            self.customerrepo.pay_money(name, amount)

            print(f"rahat on siirretty {name}")

        else:
            return "viallinen rahamäärä"

        return f"asiakkaalle {name} on maksettu {float(amount) / 100} euroa"

    def maksa_asiakkaalle_kaikki(self, name):
        """paying entire investment to customer
        Args: 
            name: to who we pay
        """
        customer = self.customerrepo.pay_all_money(name=name)
        return f"asiakkaalle {name}, on maksettu kaikki {float(customer.balance) / 100} euroa"

    def muuta_rahaston_saldoa(self, amount):
        """changing fund balance
        Args: 
            amount: how much we add to balance
        """
        if amount >= 0:
            self.balance = self.balance + amount

        else:
            return "viallinen rahamäärä"

        return f"rahastoon lisätty {amount/100} euroa"

    def paljonko_rahaa_rahastossa(self):
        """how much the is money in fund
        return: float(balance)
        """
        balance = self.customerrepo.count_money()

        return balance

    def muuta_asiakkaan_saldo(self, name, amount):
        """changing customer balance
        Args: 
            name: whos balance we change
            balance: how much we change
        """
        if amount >= 0:
            customer = Asiakas(name, amount)
            self.customerrepo.add_money(customer)

            self.muuta_rahaston_saldoa(amount)
            return f"asiakkalle: {name}, lisätty: {amount} saldoa"

        return "viallinen rahamäärä"

    def nayta_asiakkaat_ja_varat(self):
        """return entire list of customers with their funds"""
        customers = self.customerrepo.find_all()
        for customer in customers:
            print("asiakas:", customer.name, ", varat:",
                  float(customer.balance) / 100, "euroa.")

        return f"rahastossa on {float(self.balance) / 100} euroa"

    def lisaa_rahaston_omiavaroja(self, amount):
        """add balance to funds personal funds
        Args: 
            balance: how much we change
        """
        fund = Asiakas("rahaston omat", amount)
        doesfundexist = self.customerrepo.find_customer("rahaston omat")
        if doesfundexist is None:
            self.customerrepo.create(fund)
        else:
            self.customerrepo.add_money(fund)

        return f"rahaston omia varoja lisätty: {float(amount / 100)} euroa"

    def pyorita_vuosi_rahastoa(self):
        """this method mimics year cycle where fund gains 7% profit,
        and distributes gains to customers balances"""

        customers = self.customerrepo.find_all()
        for customer in customers:
            newbalance = float(customer.balance) * 0.07
            self.muuta_asiakkaan_saldo(customer.name, newbalance)

        self.ota_vuosimaksu()
        self.historia.tallenna_vuosi_tiedot()
        return "vuosi mennyt"

    def ota_vuosimaksu(self):
        """annual payment from customers 2% is taken and added to 
        funds personal balance"""
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
        """delete fund"""
        self.customerrepo.delete_fund()

        return "rahasto nollattu"

    def __str__(self):
        """forms string how much fund has balance in its entirety"""
        balance = self.paljonko_rahaa_rahastossa()
        return f"rahastossa on {balance/100} euroa"

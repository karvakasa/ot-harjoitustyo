from asiakas import Asiakas


class Rahasto:
    def __init__(self, saldo):
        if saldo >= 0:
            self.saldo = saldo

    def lisaa_asiakas_rahastoon(self, name, maara):

        if maara >= 0:

            asiakas = Asiakas(name, maara)
            self.saldo = self.saldo + maara
            print(f"Asiakas {asiakas} luotu")

        else:
            return False

    def __str__(self):
        saldo = self.saldo
        return f"rahastossa on {saldo/100} euroa"

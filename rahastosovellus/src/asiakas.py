class Asiakas:
    def __init__(self, name, saldo):
        self.saldo = saldo
        self.name = name


    def __str__(self):
        saldo_euroissa = round(self.saldo / 100, 2)

        return  "{} on rahaa {:0.2f} euroa".format(self.name, saldo_euroissa)
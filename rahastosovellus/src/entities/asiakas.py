class Asiakas:
    def __init__(self, name, balance):
        self.balance = balance
        self.name = name

    def __str__(self):
        balance_euros = round(self.balance / 100, 2)

        return "{} on rahaa {:0.2f} euroa".format(self.name, balance_euros)

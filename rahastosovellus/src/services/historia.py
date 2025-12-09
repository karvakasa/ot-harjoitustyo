import os
from repositories.rahasto_historia_repository import AsiakasHistoriaRepository

historydir = os.path.dirname(__file__)


class Historia:
    def __init__(self):
        """crete balance for fund and find file from filepath
        Args: 
            balance: how much is the starting balance of fund
        """
        self.customerhistoryrepo = AsiakasHistoriaRepository(
            os.path.join(historydir, "../../", "data", "asiakashistoria.csv"))

    def tallenna_vuosi_tiedot(self):
        self.customerhistoryrepo.write()

        return "tiedot tallennettu"

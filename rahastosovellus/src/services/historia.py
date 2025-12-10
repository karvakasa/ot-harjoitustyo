import os
from repositories.rahasto_historia_repository import AsiakasHistoriaRepository

historydir = os.path.dirname(__file__)


class Historia:
    def __init__(self):
        self.customerhistoryrepo = AsiakasHistoriaRepository(
            os.path.join(historydir, "../../", "data", "asiakashistoria.csv"))

    def tallenna_vuosi_tiedot(self):
        self.customerhistoryrepo.write()

        return "tiedot tallennettu"

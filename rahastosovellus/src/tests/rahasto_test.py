import unittest
from services.rahasto import Rahasto
from repositories.asiakas_repository import AsiakasRepository


class TestRahasto(unittest.TestCase):
    def setUp(self):
        self.rahasto = Rahasto(0)
        self.rahasto.poista_rahasto()

    def test_hello_world(self):
        self.assertEqual("Hello world", "Hello world")

    def test_luo_rahasto(self):
        pankki = Rahasto(100)
        self.assertEqual(pankki.balance, 100)

    def test_luo_viallinen_rahasto(self):
        Rahasto(balance=-5)
        self.assertEqual(self.rahasto.balance, 0)

    def test_lisaa_asiakas(self):
        self.rahasto.lisaa_asiakas_rahastoon(
            name="topias tumpelo", amount=50000)
        self.assertEqual(self.rahasto.nayta_asiakkaat_ja_varat(),
                         "rahastossa on 500.0 euroa")

    def test_nayta_asiakkaan_varat(self):
        self.rahasto.lisaa_asiakas_rahastoon("topias titunen", 5000)
        self.assertEqual(str(self.rahasto), "rahastossa on 50.0 euroa")

    def test_maksa_kaikki_rahat_asiakkaalle(self):
        self.rahasto.lisaa_asiakas_rahastoon(
            name="testi testinen", amount=1000)
        self.assertEqual(self.rahasto.maksa_asiakkaalle_kaikki(name="testi testinen"),
                         "asiakkaalle testi testinen, on maksettu kaikki 10.0 euroa")

    def test_lisaa_rahaston_omia_varoja(self):
        self.assertEqual(
            self.rahasto.lisaa_rahaston_omiavaroja(amount=5000), "rahaston omia varoja lisätty: 50.0 euroa")

    def test_pyorita_rahastoa_vuosi(self):
        self.rahasto.lisaa_asiakas_rahastoon(name="tuli leija", amount=5000)
        self.assertEqual(self.rahasto.pyorita_vuosi_rahastoa(), "vuosi mennyt")

    def test_muuta_virheellisesti_rahaston_saldoa(self):
        self.assertEqual(self.rahasto.muuta_rahaston_saldoa(
            amount=-5), "viallinen rahamäärä")

    def test_muuta_asiakkaan_saldoa(self):
        self.rahasto.lisaa_asiakas_rahastoon(name="titti tetti", amount=5000)
        self.assertEqual(self.rahasto.muuta_asiakkaan_saldo(
            name="titti tetti", amount=5000), "asiakkalle: titti tetti, lisätty: 5000 saldoa")

    def test_muuta_asiakkaan_saldoa_virheellisesti(self):
        self.assertEqual(self.rahasto.muuta_asiakkaan_saldo(
            name="titti tetti", amount=-5), "viallinen rahamäärä")

    def test_lisaa_virheellinen_asiakas(self):
        self.rahasto.lisaa_asiakas_rahastoon(name="Topias vääränen", amount=-5)
        self.assertEqual(str(self.rahasto), "rahastossa on 0.0 euroa")

    def test_maksa_asiakkaalle_rahaa(self):
        self.rahasto.lisaa_asiakas_rahastoon(
            name="topias testinen", amount=5000)
        self.assertEqual(self.rahasto.maksa_asiakkaalle_rahaa(
            "topias testinen", 5000), "asiakkaalle topias testinen on maksettu 50.0 euroa")

    def test_maksa_asiakkaalle_virheellinen_rahaa(self):
        self.rahasto.lisaa_asiakas_rahastoon(
            name="topias testinen", amount=5000)
        self.assertEqual(self.rahasto.maksa_asiakkaalle_rahaa(
            name="topias testinen", amount=-5), "viallinen rahamäärä")

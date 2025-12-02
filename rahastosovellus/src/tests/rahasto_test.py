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
        assert pankki.balance == 100

    def test_luo_viallinen_rahasto(self):
        Rahasto(-100)
        self.assertRaises(Exception, "viallinen rahamäärä")

    def test_lisaa_asiakas(self):
        self.rahasto.lisaa_asiakas_rahastoon(
            name="topias tumpelo", amount=50000)
        self.assertEqual(str(self.rahasto), "rahastossa on 500.0 euroa")

    def test_lisaa_virheellinen_asiakas(self):
        self.rahasto.lisaa_asiakas_rahastoon(name="Topias vääränen", amount=-5)
        self.assertEqual(str(self.rahasto), "rahastossa on 0.0 euroa")

    def test_maksa_asiakkaalle_rahaa(self):
        self.rahasto.lisaa_asiakas_rahastoon(
            name="topias testinen", amount=5000)
        self.rahasto.maksa_asiakkaalle_rahaa("topias testinen", 5000)
        self.assertRaises(
            Exception, "asiakkaalle topias testinen, on maksettu kaikki 500.0 euroa")

    def test_maksa_asiakkaalle_virheellinen_rahaa(self):
        self.rahasto.lisaa_asiakas_rahastoon(
            name="topias testinen", amount=5000)
        self.rahasto.maksa_asiakkaalle_rahaa("topias testinen", -5000)
        self.assertRaises(Exception, "viallinen rahamäärä")

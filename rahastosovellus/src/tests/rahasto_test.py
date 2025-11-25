import unittest
from rahasto import Rahasto


class TestRahasto(unittest.TestCase):
    def setUp(self):
        self.rahasto = Rahasto(0)

    def test_hello_world(self):
        self.assertEqual("Hello world", "Hello world")

    def test_luo_rahasto(self):
        pankki = Rahasto(100)
        assert pankki.saldo == 100

    def test_lisaa_asiakas(self):
        self.rahasto.lisaa_asiakas_rahastoon(name="Topias Tallberg", maara=50000)
        self.assertEqual(str(self.rahasto), "rahastossa on 500.0 euroa")

    def test_lisaa_virheellinen_asiakas(self):
        self.rahasto.lisaa_asiakas_rahastoon(name="Topias Tallberg", maara=-5)
        self.assertEqual(str(self.rahasto), "rahastossa on 0.0 euroa")

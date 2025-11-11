import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(self.maksukortti.saldo, 2000)

    def test_rahan_ottaminen_toimii_kun_riittavasti_rahaa(self):
        self.maksukortti.ota_rahaa(500)

        self.assertTrue(self.maksukortti.saldo, 500)

    def test_rahan_ottaminen_ei_toimi_kun_rahaa_ei_riittavasti(self):
        self.maksukortti.ota_rahaa(1500)

        self.assertTrue(self.maksukortti.saldo_euroina, 10)

    def test_saldo_euroissa_toimii(self):
        kortti = self.maksukortti.saldo_euroina()

        self.assertEqual(kortti, 10)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

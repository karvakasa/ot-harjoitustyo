import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassan_alkuarvo(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassan_alkuarvo_euroina(self):
        eurot = self.kassapaate.kassassa_rahaa_euroina()
        self.assertEqual(eurot, 1000.0)

    def test_edulliset_ateriat_alkuarvo(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_ateriat_alkuarvo(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kateisella_toimii(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kateisella_ei_toimii(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kateisella_toimii(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kateisella_ei_toimii(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_maukkaasti_kortilla_toimii(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kortilla_ei_toimii(self):
        self.maksukortti.ota_rahaa(700)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kortilla_toimii(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kortilla_ei_toimii(self):
        self.maksukortti.ota_rahaa(800)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_lataa_rahaa_kortille_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertTrue(self.maksukortti.saldo, 1500)

    def test_lataa_miinus_rahaa_kortille_ei_toimi(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -500)
        self.assertTrue(self.maksukortti.saldo, 1000)

import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luodaan_uusi_kassapaate(self):
        self.assertNotEqual(self.kassapaate.kassassa_rahaa, 10000)

    def test_kateisosto_edullisesti_toimii(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(600), 360)

    def test_kateisosto_maukkaasti_toimii(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(600), 200)
    
    def test_kateisosto_maukkaasti_eitoimi(self):
        Kassapaate.syo_maukkaasti_kateisella(self, 99)
    
    def test_kateisosto_edullisesti_eitoimi(self):
        Kassapaate.syo_edullisesti_kateisella(self, 1)
    
    def test_korttiosto_maukkaasti_toimii(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_korttiosto_maukkaasti_eitoimi(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)

    def test_korttiosto_edullisesti_toimii(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_korttiosto_edullisesti_eitoimi(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)

    def test_lataa_negatiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -10)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_lataa_positiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 10)
        self.assertEqual(str(self.maksukortti), "saldo: 10.1")
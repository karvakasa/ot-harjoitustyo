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

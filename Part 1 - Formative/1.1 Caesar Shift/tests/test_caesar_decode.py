from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caesar_decode



class TestCaesarDecode(TestCase):
    def test_spaces(self):
        self.assertEqual(caesar_decode("KHO OR", 3), "HEL LO")

    def test_lowercase(self):
        self.assertEqual(caesar_decode("khoor", 3), "hello")

    def test_one_capital(self):
        self.assertEqual(caesar_decode("Khoor", 3), "Hello")

    def test_two_numbers(self):
        self.assertEqual(caesar_decode("2", 2), "2")

    def test_switched_values(self):
        self.assertEqual(caesar_decode("3", "HELLO"), "3")

    def test_puncuations(self):
        self.assertEqual(caesar_decode("KHOOR!", 3), "HELLO!")

    def test_everything(self):
        self.assertEqual(caesar_decode("khO Or!>&6", 3), "heL Lo!>&6")

    # add assertion here



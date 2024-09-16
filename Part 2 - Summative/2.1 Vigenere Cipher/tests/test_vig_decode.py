from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_decode



class TestVigDecode(TestCase):
    def test_spaces(self):
        self.assertEqual(vig_decode("LLRX", "TEST"), "TH E")

    def test_lowercase(self):
        self.assertEqual(vig_decode("llw", "TEST"), "the")

    def test_one_capital(self):
        self.assertEqual(vig_decode("Llw", "TEST"), "The")

    def test_two_numbers(self):
        self.assertEqual(vig_decode("2", "TEST"), "2")

    def test_puncuations(self):
        self.assertEqual(vig_decode("LLW!", "TEST"), "THE!")

    def test_everything(self):
        self.assertEqual(vig_decode("LLRx!>&6", "TEST"), "TH e!>&6")

    def test_length(self):
        self.assertEqual(vig_decode("LLW", "A"), "LLW")

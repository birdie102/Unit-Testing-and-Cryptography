from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import vig_encode



class TestVigEncode(TestCase):
    def test_spaces(self):
        self.assertEqual(vig_encode("TH E", "TEST"), "LLR")

    def test_lowercase(self):
        self.assertEqual(vig_encode("the", "TEST"), "llw")

    def test_one_capital(self):
        self.assertEqual(vig_encode("The", "TEST"), "Llw")

    def test_two_numbers(self):
        self.assertEqual(vig_encode("2", "TEST"), "2")

    def test_puncuations(self):
        self.assertEqual(vig_encode("THE!", "TEST"), "LLW!")

    def test_everything(self):
        self.assertEqual(vig_encode("TH e!>&6", "TEST"), "LL w!>&6")

    def test_length(self):
        self.assertEqual(vig_encode("THE", "A"), "THE")

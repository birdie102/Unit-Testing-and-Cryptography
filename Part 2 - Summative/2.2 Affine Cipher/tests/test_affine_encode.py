from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_encode



class TestAffineEncode(TestCase):
    def test_spaces(self):
        self.assertEqual(affine_encode("HELLO WORLD", 3, 9), "EVQQZXZIQS")

    def test_lowercase(self):
        self.assertEqual(affine_encode("helloworld", 3, 9), "EVQQZXZIQS")

    def test_one_capital(self):
        self.assertEqual(affine_encode("Helloworld", 3, 9), "EVQQZXZIQS")

    def test_two_numbers(self):
        self.assertEqual(affine_encode("2", 3, 9), "")

    def test_puncuations(self):
        self.assertEqual(affine_encode("HELLOWORLD!", 3, 9), "EVQQZXZIQS")

    def test_everything(self):
        self.assertEqual(affine_encode("HELLO WORLd!>&6", 3, 9), "EVQQZXZIQS")



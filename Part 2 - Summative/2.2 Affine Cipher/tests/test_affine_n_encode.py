from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_n _encode



class TestAffineNEncode(TestCase):
    def test_spaces(self):
        self.assertEqual(affine_n_encode("EVQQZ XZIQS", 3, 9), "HELLOWORLD")

    def test_lowercase(self):
        self.assertEqual(affine_n_encode("evqqzxziqs", 3, 9), "HELLOWORLD")

    def test_one_capital(self):
        self.assertEqual(affine_n_encode("Evqqzxziqs", 3, 9), "HELLOWORLD")

    def test_two_numbers(self):
        self.assertEqual(affine_n_encode("2", 3, 9), "")

    def test_puncuations(self):
        self.assertEqual(affine_n_encode("EVQQZXZIQS!", 3, 9), "HELLOWORLD")

    def test_everything(self):
        self.assertEqual(affine_n_encode("EVQQ ZXZIQs!>&6", 3, 9), "HELLOWORLD")



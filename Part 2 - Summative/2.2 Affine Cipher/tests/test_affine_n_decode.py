from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import affine_n_decode



class TestAffineNDecode(TestCase):
    def test_cool(self):
        self.assertEqual(affine_n_decode("XUHN", 2, 3, 121), "COOL")

    def test_coolxx(self):
        self.assertEqual(affine_n_decode("XURYWT", 3, 3, 121), "COOLXX")




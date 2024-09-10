from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_decode



class TestSubDecode(TestCase):
    def test_spaces(self):
        self.assertEqual(sub_decode("MXT TH", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "HEL LO")

    def test_lowercase(self):
        self.assertEqual(sub_decode("mxtth", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "hello")

    def test_one_capital(self):
        self.assertEqual(sub_decode("Mxtth", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "Hello")

    def test_two_numbers(self):
        self.assertEqual(sub_decode("2", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "2")

    def test_puncuations(self):
        self.assertEqual(sub_decode("MXTTH!", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "HELLO!")

    def test_everything(self):
        self.assertEqual(sub_decode("mxT Th!>&6", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "heL Lo!>&6")

    def test_length(self):
        self.assertEqual(sub_decode("HELLO", "A"), "HELLO")

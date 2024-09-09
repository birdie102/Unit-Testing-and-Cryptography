from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_encode



class TestSubEncode(TestCase):
    def test_spaces(self):
        self.assertEqual(sub_encode("HEL LO", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "MXT TH")

    def test_lowercase(self):
        self.assertEqual(sub_encode("hello", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "mxtth")

    def test_one_capital(self):
        self.assertEqual(sub_encode("Hello", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "Mxtth")

    def test_two_numbers(self):
        self.assertEqual(sub_encode("2", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "2")

    def test_puncuations(self):
        self.assertEqual(sub_encode("HELLO!", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "MXTTH!")

    def test_everything(self):
        self.assertEqual(sub_encode("heL Lo!>&6", "WJKUXVBMIYDTPLHZGONCRSAEFQ"), "MxT Th!>&6")

    def test_length(self):
        self.assertEqual(sub_encode("HELLO", "A"), "HELLO")

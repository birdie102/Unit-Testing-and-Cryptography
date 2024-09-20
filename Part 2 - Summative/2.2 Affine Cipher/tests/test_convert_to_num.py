from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import convert_to_num



class TestConvertToNum(TestCase):
    def test_spaces(self):
        self.assertEqual(convert_to_num("B C"), 53)

    def test_lowercase(self):
        self.assertEqual(convert_to_num("helloworld", 3, 9), "EVQQZXZIQS")

    def test_one_capital(self):
        self.assertEqual(convert_to_num("Helloworld", 3, 9), "EVQQZXZIQS")

    def test_two_numbers(self):
        self.assertEqual(convert_to_num("2", 3, 9), "")

    def test_puncuations(self):
        self.assertEqual(convert_to_num("HELLOWORLD!", 3, 9), "EVQQZXZIQS")

    def test_everything(self):
        self.assertEqual(convert_to_num("HELLO WORLd!>&6", 3, 9), "EVQQZXZIQS")



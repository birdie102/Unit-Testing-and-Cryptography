
from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import caeser_encode



class TestCaesarEncode(TestCase):
    def test_spaces(self):
        self.assertEqual(caesar_encode("HEL LO", 3), "KHO OR")

    def test_lowercase(self):
        self.assertEqual(caesar_encode("hello", 3), "khoor")

    def test_one_capital(self):
        self.assertEqual(caesar_encode("Hello", 3), "Khoor")

    def test_two_numbers(self):
        self.assertEqual(caesar_encode(2, 2), "2")

    def test_switched_values(self):
        self.assertEqual(caesar_encode(3, "HELLO"), "3")
    # add assertion here



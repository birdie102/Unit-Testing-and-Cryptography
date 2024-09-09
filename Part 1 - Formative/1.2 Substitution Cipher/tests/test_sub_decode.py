from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sub_decode



class TestSubDecode(TestCase):
    def test_spaces(self):
        self.assertEqual(sub_decode("HEL LO", 3), "KHO OR")

from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import convert_to_text



class TestConvertToText(TestCase):
    def test_cb(self):
        self.assertEqual(convert_to_text(28, 2), "CB")

    def test_bc(self):
        self.assertEqual(convert_to_text(53, 2), "BC")

    def test_bark(self):
        self.assertEqual(convert_to_text(187253, 4), "BARK")

    def test_long(self):
        self.assertEqual(convert_to_text(218741750267309021256255930435388550208768849997977, 36), "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG")




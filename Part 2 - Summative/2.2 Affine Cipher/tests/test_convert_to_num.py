from unittest import TestCase
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import convert_to_num



class TestConvertToNum(TestCase):
    def test_cb(self):
        self.assertEqual(convert_to_num("CB"), 28)

    def test_bc(self):
        self.assertEqual(convert_to_num("BC"), 53)

    def test_bark(self):
        self.assertEqual(convert_to_num("BARK"), 187253)

    def test_long(self):
        self.assertEqual(convert_to_num("THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"), 218741750267309021256255930435388550208768849997977)




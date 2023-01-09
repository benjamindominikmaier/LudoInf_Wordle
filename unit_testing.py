#!/usr/bin/env python3.9
# -*- coding: utf-8 -*

# project/
# │
# ├── code/
# │   ├── file_1.py
# │   └── file_2.py
# │
# └── tests.py

# assertEqual(a, b) 	    a == b
# assertNotEqual(a, b) 	    a != b
# assertTrue(x) 	        bool(x) is True
# assertFalse(x) 	        bool(x) is False
# assertIs(a, b) 	        a is b
# assertIsNot(a, b) 	    a is not b
# assertIsNone(x) 	        x is None
# assertIsNotNone(x) 	    x is not None
# assertIn(a, b) 	        a in b
# assertNotIn(a, b) 	    a not in b
# assertIsInstance(a, b) 	isinstance(a, b)
# assertNotIsInstance(a, b) not isinstance(a, b)



import unittest
from unittest.mock import patch
from wordle import input_word


class TestSum(unittest.TestCase):
    word_list = ["Benni", "Lasse", "Clemen", "ANTON"]

    # def test_sum(self):
    #     self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
    #     # assert sum([1,2,3]) == 6, "Should be 6"
    # def test_sum_tuple(self):
    #     self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
    #
    # def erste_lab_testfunktion(self):
    #     pass
    #
    # def zweite_lab_testfunktion(self):
    #     pass

    @patch('builtins.input', lambda *args: 'Anton')
    def test_richtige_laenge(self):
        antwort = input_word(self.word_list, 5)
        self.assertEqual(len(antwort), 5)



if __name__ == '__main__':
    unittest.main()

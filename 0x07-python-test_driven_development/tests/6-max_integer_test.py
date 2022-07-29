#!/usr/bin/python3

import unittest

max_integer = __import__('6-max_integer').max_integer

class max_integer_test(unittest.TestCase):
    def test_nullable_parameter(self):
        """ test_nullable_parameter function
        this function test all posibilities with empty list
        """
        self.assertIsNone(max_integer())
        self.assertIsNone(max_integer([]))

    def test_integer_format(self):
        """ test_integer_format function
        this function test all posibilities with integer
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)              # sorted values
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)              # unsorted values
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)              # inversed values
        self.assertEqual(max_integer([4]), 4)                       # one value
        self.assertEqual(max_integer([4, 4, 4, 3, 1, 1, 2, 0]), 4)  # repetitive values

    def test_character_format(self):
        """ test_character_format function
        this function test all posibilities with character
        """
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')                        # sorted character format
        self.assertEqual(max_integer(['c', 'b', 'a', 'd']), 'd')                        # unsorted character format
        self.assertEqual(max_integer(['d', 'c', 'b', 'a']), 'd')                        # inversed character format
        self.assertEqual(max_integer(['d', 'd', 'd', 'c', 'e', 'e', 'b', 'a']), 'e')    # repetitive values

    def test_float_format(self):
        """ test_float_format function
        this function test all posibilities with float
        """
        self.assertEqual(max_integer([1.0, 1.2, 1.4, 1.6, 1.8]), 1.8)       # sorted float values
        self.assertEqual(max_integer([1.0, 3.0, 4.0, 2.0]), 4.0)            # unsorted float values
        self.assertEqual(max_integer([1.8, 1.6, 1.4, 1.2, 1.0]), 1.8)       # inversed float values
        self.assertEqual(max_integer([-1.0, -1.2, -1.4, -1.6, -1.8]), -1.0) # sorted negative float values
        self.assertEqual(max_integer([-1.8, -1.6, -1.4, -1.2, -1.0]), -1.0) # inversed negative float values
        self.assertEqual(max_integer([-1.0, -3.0, -4.0, -2.0]), -1.0)       # unsorted negative float values
        self.assertEqual(max_integer([-1.0, 3, -4.0, -2.0]), 3)             # share float and integer format

    def test_wrong_format(self):
        """ test_wrong_format function
        this function test all posibilities with both format
        """
        with self.assertRaises(TypeError):
            max_integer(['a', 'b', 'c', 'd', -1.0, -1.2, -1.4, -1.6, -1.8]) # both format

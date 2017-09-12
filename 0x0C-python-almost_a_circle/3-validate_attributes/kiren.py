#!/usr/bin/python3
"""
Unit tests for Rectangle class
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Initialization tests with invalid arguments"""
    def test_bad_height(self):
        with self.assertRaises(TypeError) as cm:
            self.rect = Rectangle(10, "2")

    def test_bad_width(self):
        with self.assertRaises(ValueError) as cm:
            self.rect = Rectangle(-10, 2)

    def test_bad_x(self):
        with self.assertRaises(TypeError) as cm:
            self.rect = Rectangle(10, 2, {})

    def test_bad_y(self):
        with self.assertRaises(ValueError) as cm:
            self.rect = Rectangle(10, 2, 3, -1)

if __name__ == "__main__":
    unittest.main()

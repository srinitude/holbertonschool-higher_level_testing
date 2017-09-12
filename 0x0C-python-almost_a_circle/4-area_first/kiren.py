#!/usr/bin/python3
"""
Unit tests for Rectangle class
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Area"""
    def test_area(self):
        self.rect = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(self.rect.area(), 56)

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""
Unit tests for Rectangle class
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Initialization tests with valid arguments"""
    def test_valid_height_width(self):
        rect = Rectangle(10, 2)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 2)

    def test_all_valid_params(self):
        rect = Rectangle(10, 2, 3, 4, 12)
        self.assertEqual(rect.id, 12)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 2)

    """Initialization tests with invalid arguments"""
    with self.assertRaises(TypeError):
        rect = Rectangle(10, "2")

    with self.assertRaises(ValueError):
        rect = Rectangle(-10, 2)

    with self.assertRaises(TypeError):
        rect = Rectangle(10, 2, {})

    with self.assertRaises(ValueError):
        rect = Rectangle(10, 2, 3, -1)

if __name__ == "__main__":
    unittest.main()

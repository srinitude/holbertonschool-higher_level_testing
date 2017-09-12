#!/usr/bin/python3
"""
Unit tests for Rectangle class
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
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

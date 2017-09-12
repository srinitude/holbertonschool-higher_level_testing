#!/usr/bin/python3
"""
Unit tests for Rectangle class
"""


import unittest
from models import rectangle
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Presence of docstrings"""
    def test_presence_of_module_docstring(self):
        module_doc = rectangle.__doc__
        self.assertTrue(len(module_doc) > 1)

    def test_presence_of_class_docstring(self):
        class_doc = Rectangle.__doc__
        self.assertTrue(len(class_doc) > 1)

    def test_presence_of_init_docstring(self):
        init_doc = Rectangle.__init__.__doc__
        self.assertTrue(len(init_doc) > 1)

    def test_presence_of_str_docstring(self):
        str_doc = Rectangle.__str__.__doc__
        self.assertTrue(len(str_doc) > 1)

    def test_presence_of_width_docstring(self):
        width_doc = Rectangle.width.__doc__
        self.assertTrue(len(width_doc) > 1)

    def test_presence_of_height_docstring(self):
        height_doc = Rectangle.height.__doc__
        self.assertTrue(len(height_doc) > 1)

    def test_presence_of_x_docstring(self):
        x_doc = Rectangle.x.__doc__
        self.assertTrue(len(x_doc) > 1)

    def test_presence_of_y_docstring(self):
        y_doc = Rectangle.y.__doc__
        self.assertTrue(len(y_doc) > 1)

    def test_presence_of_area_docstring(self):
        area_doc = Rectangle.area.__doc__
        self.assertTrue(len(area_doc) > 1)

    def test_presence_of_display_doc(self):
        disp_doc = Rectangle.display.__doc__
        self.assertTrue(len(disp_doc) > 1)

    def test_presence_of_update_doc(self):
        up_doc = Rectangle.update.__doc__
        self.assertTrue(len(up_doc) > 1)

    def test_presence_of_to_dict_doc(self):
        td_doc = Rectangle.to_dictionary.__doc__
        self.assertTrue(len(td_doc) > 1)

    """Initialization tests"""
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

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Test suite for BaseModel class"""
import unittest
from unittest import mock
from models.base_model import BaseModel
from models.base_model import __doc__ as module_level_doc
from datetime import datetime
import re

class TestBaseModel(unittest.TestCase):
    """Series of unit tests to test core functions of BaseModel"""
    def test_docstrings(self):
        """Test for documentation"""
        self.assertIsNotNone(module_level_doc)
        self.assertIsNotNone(BaseModel.__doc__)
        # Expected attributes of BaseModel
        attrs = ["__init__",
                 "__str__",
                 "id",
                 "created_at",
                 "updated_at",
                 "save",
                 "to_dict"]
        for attr in attrs:
            with self.subTest(attr=attr):
                # Check that attr exists
                self.assertIs(hasattr(BaseModel, attr), True)
                # Check for non-empty docstring
                self.assertIsNotNone(getattr(BaseModel, attr + ".__doc__"))
                # Check that docstring length is greater than 1
                self.assertGreater(getattr(BaseModel, attr + ".__doc__"), 1)

    def test_instantiation(self):
        """Test that instantiation works as expected"""
        my_model = BaseModel()
        self.assertTrue(type(my_model) == BaseModel)
        my_model.name = "Holberton"
        my_model.my_number = 89
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "my_number"]
        self.assertCountEqual(my_model.__dict__.keys(), expected_attrs)
        self.assertEqual(getattr(my_model, 'name'), "Holberton")
        self.assertEqual(getattr(my_model, 'my_number'), 89)
        self.assertEqual(getattr(my_model, 'created_at'),
                         getattr(my_model, 'updated_at'))

    def test_uuid(self):
        """Test that id is a valid uuid"""
        my_model1 = BaseModel()
        my_model2 = BaseModel()
        self.assertRegex(my_model1.id,
                         '^[0-9a-f]{8}-[0-9a-f]{4}'
                         '-[0-9a-f]{4}-[0-9a-f]{4}'
                         '-[0-9a-f]{12}$')
        self.assertNotEqual(my_model1.id, my_model2.id)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        d = my_model.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "my_number",
                          "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['name'], "Holberton")
        self.assertEqual(d['my_number'] = 89)

    def test_date(self):
        """Test use of datetime for `created_at` attribute"""
        my_model = BaseModel()
        now = datetime.now()
        self.assertTrue(type(my_model.created_at) == type(now))
        self.assertTrue(type(my_model.updated_at) == type(now))
        self.assertEqual(my_model.created_at, my_model.updated_at)
        delta = now - my_model.created_at
        self.assertAlmostEqual(delta.total_seconds(), 0.0, delta = 1e-2)

    def test_save(self):
        """Test of the save method, which updates `updated_at` attribute"""
        my_model = BaseModel()
        self.assertEqual(my_model.created_at, my_model.updated_at)
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

#!/usr/bin/python3
from datetime import datetime
import inspect
from models import base_model
import pep8
import unittest
import string
BaseModel = base_model.BaseModel


class TestBaseModelDocs(unittest.TestCase):
    """Tests to check the documentation and style of BaseModel class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_f = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8_conformance_base_model(self):
        """Test that models/base_model.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_base_model(self):
        """Test that tests/test_models/test_base_model.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_bm_module_docstring(self):
        """Test for the base_model.py module docstring"""
        self.assertIsNot(base_model.__doc__, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(base_model.__doc__) >= 1,
                        "base_model.py needs a docstring")

    def test_bm_class_docstring(self):
        """Test for the BaseModel class docstring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_bm_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for func in self.base_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def test_is_base_model(self):
        """test that the instatiation of a BaseModel works"""
        base_model = BaseModel()
        self.assertEqual(type(base_model), BaseModel)

    def test_created_at_instantiation(self):
        """test created_at is a pub. instance attribute of type datetime"""
        base_model = BaseModel()
        self.assertTrue(base_model.created_at is not None)
        self.assertEqual(type(base_model.created_at), datetime)

    def test_updated_at_instantiation(self):
        """test updated_at is a pub. instance attribute of type datetime"""
        base_model = BaseModel()
        self.assertTrue(base_model.updated_at is not None)
        self.assertEqual(type(base_model.updated_at), datetime)

    def test_diff_datetime_objs(self):
        """test that two BaseModel instances have different datetime objects"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.created_at, bm2.created_at)
        self.assertNotEqual(bm1.updated_at, bm2.updated_at)

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
        self.assertEqual(d['my_number'], 89)

    def test_date_differences(self):
        """Test use of datetime for `created_at` attribute"""
        my_model = BaseModel()
        now = datetime.now()
        self.assertTrue(type(my_model.created_at) == type(now))
        self.assertTrue(type(my_model.updated_at) == type(now))
        self.assertEqual(my_model.created_at, my_model.updated_at)
        delta = now - my_model.created_at
        self.assertAlmostEqual(delta.total_seconds(), 0.0, delta=1e-2)

    def test_valid_UUID_creation(self):
        '''test created_at is a saloon.'''
        bm = BaseModel()
        id = bm.id
        allhex = id.split('-')
        # id is a string
        self.assertIs(type(id), str)
        # len(id) = 37
        self.assertIs(len(id), 36)
        # dash at 8, 13, 18, 23 indexes
        self.assertIs(id[8], "-")
        self.assertIs(id[13], "-")
        self.assertIs(id[18], "-")
        self.assertIs(id[23], "-")

        # all hex characters between dashes
        for substring in allhex:
            self.assertIs(all(c in string.hexdigits for c in substring), True)

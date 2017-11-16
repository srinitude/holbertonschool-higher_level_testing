#!/usr/bin/python3
"""
Test the database version of City
"""
from os import environ
environ["HBNB_TYPE_STORAGE"] = "db"
from models import city
from models.base_model import BaseModel
from datetime import datetime
import unittest
City = city.City


class TestCity_db(unittest.TestCase):
    """Test the City class with db storage"""

    attributes = {}

    row = City(**attributes)

    def test_mysql_obj(self):
        """Test that instance ORM object"""
        self.assertTrue(hasattr(self.row, '_sa_instance_state'))

    def test_table_name(self):
        """Test that table name is cities"""
        self.assertEqual(self.row.__tablename__, "cities")

    def test_time_obj(self):
        """Test that created_at and updated_at is date and time object"""
        self.assertTrue(type(self.row.created_at), datetime)
        self.assertTrue(type(self.row.updated_at), datetime)


    def test_isChild(self):
        """Test if instance is child of City"""
        self.assertIsInstance(self.row, City)

    def test_attributes(self):
        """Test for required attr for table cities"""
        self.attributes.update({'id': None, 'places': None})
        for attr in self.attributes.keys():
            with self.subTest(attr=attr):
                self.assertTrue(hasattr(self.row, attr))

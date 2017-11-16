#!/usr/bin/python3
"""
Test the database version of State
"""
from os import environ
environ["HBNB_TYPE_STORAGE"] = "db"
from models import state
from models.base_model import BaseModel
from datetime import datetime
import unittest
State = state.State


class TestState_db(unittest.TestCase):
    """Test the State class with db storage"""

    attributes = { 'name': "California" }

    row = State(**attributes)

    def test_mysql_obj(self):
        """Test that instance ORM object"""
        self.assertTrue(hasattr(self.row, '_sa_instance_state'))

    def test_table_name(self):
        """Test that table name is states"""
        self.assertEqual(self.row.__tablename__, "states")

    def test_time_obj(self):
        """Test that created_at and updated_at is date and time object"""
        self.assertTrue(type(self.row.created_at), datetime)
        self.assertTrue(type(self.row.updated_at), datetime)
        self.assertEqual(type(self.row), State)


    def test_isChild(self):
        """Test if instance is child of State"""
        self.assertIsInstance(self.row, State)

    def test_attributes(self):
        """Test for required attr for table states"""
        self.attributes.update({'id': None, 'cities': None})
        for attr in self.attributes.keys():
            with self.subTest(attr=attr):
                self.assertTrue(hasattr(self.row, attr))

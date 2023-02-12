#!/usr/bin/python3
"""Unittest module for the FileStorage class."""

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import re
import json
import os


class TestFileStorage(unittest.TestCase):
    """Test Cases for the FileStorage class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def test_5_instantiation(self):
        """Tests instantiation of storage class."""
        self.assertEqual(type(storage).__name__, "FileStorage")

    def test_3_init_no_args(self):
        """Tests __init__ with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.__init__()
        msg = "descriptor '__init__' of 'object' object needs an argument"
        self.assertEqual(str(e.exception), msg)

    def test_3_init_many_args(self):
        """Tests __init__ with many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            b = FileStorage(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        msg = "object() takes no parameters"
        self.assertEqual(str(e.exception), msg)

    def test_5_attributes(self):
        """Tests class attributes."""
        self.resetStorage()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(getattr(FileStorage, "_FileStorage__objects"), {})

    def help_test_all(self, classname):
        """Helper tests all() method for classname."""
        self.resetStorage()
        self.assertEqual(storage.all(), {})

        o = storage.classes()[classname]()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        self.assertTrue(key in storage.all())
        self.assertEqual(storage.all()[key], o)

    def test_5_all_base_model(self):
        """Tests all() method for BaseModel."""
        self.help_test_all("BaseModel")

    def test_5_all_user(self):
        """Tests all() method for User."""
        self.help_test_all("User")

    def test_5_all_state(self):
        """Tests all() method for State."""
        self.help_test_all("State")

    def test_5_all_city(self):
        """Tests all() method for City."""
        self.help_test_all("City")

    def test_5_all_amenity(self):
        """Tests all() method for Amenity."""
        self.help_test_all("Amenity")

    def test_5_all_place(self):
        """Tests all() method for Place."""
        self.help_test_all("Place")

    def test_5_all_review(self):
        """Tests all() method for Review."""
        self.help_test_all("Review")

    def help_test_all_multiple(self, classname):
        """Helper tests all() method with many objects for classname."""
        self.resetStorage()
        self.assertEqual(storage.all(), {})

        cls = storage.classes()[classname]
        objs = [cls() for i in range(1000)]
        [storage.new(o) for o in objs]
        self.assertEqual(len(objs), len(storage.all()))
        for o in objs:
            key = "{}.{}".format(type(o).__name__, o.id)
            self.assertTrue(key in storage.all())
            self.assertEqual(storage.all()[key], o)

    def test_5_all_multiple_base_model(self):
        """Tests all() method with many objects."""
        self.help_test_all_multiple("BaseModel")

    def test_5_all_multiple_user(self):
        """Tests all_multiple() method for User."""
        self.help_test_all_multiple("User")

    def test_5_all_multiple_state(self):
        """Tests all_multiple() method for State."""
        self.help_test_all_multiple("State")

    def test_5_all_multiple_city(self):
        """Tests all_multiple() method for City."""
        self.help_test_all_multiple("City")

    def test_5_all_multiple_amenity(self):
        """Tests all_multiple() method for Amenity."""
        self.help_test_all_multiple("Amenity")

    def test_5_all_multiple_place(self):
        """Tests all_multiple() method for Place."""
        self.help_test_all_multiple("Place")

    def test_5_all_multiple_review(self):
        """Tests all_multiple() method for Review."""
        self.help_test_all_multiple("Review")

    def test_5_all_no_args(self):
        """Tests all() with no arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.all()
        msg = "all() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_5_all_excess_args(self):
        """Tests all() with too many arguments."""
        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.all(self, 98)
        msg = "all() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

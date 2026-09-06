#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py."""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        if os.path.exists("file.json"):
            os.remove("file.json")
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up test environment."""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Test that all() returns the __objects dictionary."""
        storage_obj = FileStorage()
        obj_dict = storage_obj.all()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict, FileStorage._FileStorage__objects)

    def test_new(self):
        """Test that new() adds an object to __objects with correct key."""
        bm = BaseModel()
        storage.new(bm)
        key = "BaseModel.{}".format(bm.id)
        self.assertIn(key, storage.all())

    def test_save_and_reload(self):
        """Test that save() serializes and reload() deserializes objects."""
        bm = BaseModel()
        user = User()
        storage.new(bm)
        storage.new(user)
        storage.save()

        self.assertTrue(os.path.exists("file.json"))

        new_storage = FileStorage()
        new_storage.reload()
        objs = new_storage.all()

        self.assertIn("BaseModel.{}".format(bm.id), objs)
        self.assertIn("User.{}".format(user.id), objs)


if __name__ == "__main__":
    unittest.main()
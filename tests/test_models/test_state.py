#!/usr/bin/python3
"""Defines unittests for models/state.py."""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_is_subclass(self):
        """Test that State is a subclass of BaseModel."""
        self.assertIsInstance(State(), BaseModel)

    def test_attribute_types(self):
        """Test State attribute types and defaults."""
        state = State()
        self.assertIsInstance(state.name, str)
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()
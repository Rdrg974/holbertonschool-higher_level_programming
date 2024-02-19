#!/usr/bin/python3
'''Module for Base unit tests.'''
import unittest
import json
import sys

from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''Tests the Base class.'''
    def test_initialisation(self):
        """Tests Base() instantiation."""
        b = Base()

        self.assertGreater(b.id, 0)

    def test_incrementation(self):
        """Test Base() incrementation"""
        a = Base()
        b = Base()

        self.assertEqual(b.id, a.id + 1)

    def test_saving_id(self):
        """Test Base(89)"""
        b = Base(89)

        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """Args is None"""
        json_dictionary = Base.to_json_string(None)

        self.assertTrue(json_dictionary, "null")

    def test_to_json_string_empty_list(self):
        """Empty list"""
        json_dictionary = Base.to_json_string([])

        self.assertTrue(json_dictionary, [])

    def test_to_json_string_id(self):
        """List contains [ { 'id': 12 }]"""
        input_data = [ { 'id': 12 }]
        expected_output = json.dumps(input_data)
        json_dictionary = Base.to_json_string(input_data)

        self.assertTrue(json_dictionary, [ { 'id': 12 }])
        self.assertEqual(json_dictionary, expected_output)

    def test_from_json_string_none(self):
        """Args is None"""
        list_output = Base.from_json_string(None)

        self.assertEqual(list_output, [])

    def test_from_json_string_empty_list(self):
        """Test for "[]"."""
        list_output = Base.from_json_string("[]")

        self.assertEqual(list_output, [])

    def test_from_json_string_id(self):
        """List contains [ { 'id': 89 }]"""
        input_data = '[ { "id": 89 }]'
        expected_output = [ { 'id': 89 }]
        json_dictionary = Base.from_json_string(input_data)

        self.assertEqual(json_dictionary, expected_output)
        self.assertIsInstance(json_dictionary, list)

    def text_create_1(self):
        """Test create Rectangle with a dict : **{ 'id': 89 }"""
        r1 = Rectangle(10, 10, 10, 10)
        r2 = Rectangle.create(**{ 'id': 89 })

        self.assertEqual(r1.id, r2.id)

if __name__ == "__main__":
    unittest.main()
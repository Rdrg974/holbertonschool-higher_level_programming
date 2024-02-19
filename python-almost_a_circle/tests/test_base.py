#!/usr/bin/python3
'''Module for Base unit tests.'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''Tests the Base class.'''
    def test_initialisation(self):
        """Tests Base() instantiation."""
        a = Base()
        b = Base()

        self.assertNotEqual(a.id, b.id)

        self.assertIsInstance(a.id, int)
        self.assertIsInstance(a.id, int)

if __name__ == "__main__":
    unittest.main()
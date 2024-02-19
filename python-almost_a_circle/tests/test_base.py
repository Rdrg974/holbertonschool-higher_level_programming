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
        b = Base()

        self.assertGreater(b.id, 0)

    def test_incrementation(self):
        """Test Base() incrementation"""
        a = Base()
        b = Base()

        self.assertEqual(b.id, a.id + 1)

if __name__ == "__main__":
    unittest.main()
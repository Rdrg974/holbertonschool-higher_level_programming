#!/usr/bin/python3
'''Module for Rectangle unit tests.'''
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestRectangle(unittest.TestCase):
    '''Tests the Rectangle class.'''
    def test_initialisation(self):
        """Initialise the rectangle"""
        r1 = Rectangle(1, 2)

        self.assertIsInstance(r1, Rectangle)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

        r2 = Rectangle(1, 2, 3)

        self.assertIsInstance(r2, Rectangle)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)

        r3 = Rectangle(1, 2, 3, 4)

        self.assertIsInstance(r3, Rectangle)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)

        with self.assertRaises(TypeError):
            r4 = Rectangle("1", 2)
        
        with self.assertRaises(TypeError):
            r5 = Rectangle(1, "2")

        with self.assertRaises(TypeError):
            r6 = Rectangle(1, 2, "3")

        with self.assertRaises(TypeError):
            r7 = Rectangle(1, 2, 3, "4")

        r8 = Rectangle(1, 2, 3, 4, 5)

        self.assertIsInstance(r8, Rectangle)
        self.assertEqual(r8.width, 1)
        self.assertEqual(r8.height, 2)
        self.assertEqual(r8.x, 3)
        self.assertEqual(r8.y, 4)
        self.assertEqual(r8.id, 5)

        with self.assertRaises(ValueError):
            r9 = Rectangle(-1, 2)

        with self.assertRaises(ValueError):
            r10 = Rectangle(1, -2)

        with self.assertRaises(ValueError):
            r11 = Rectangle(0, 2)

        with self.assertRaises(ValueError):
            r12 = Rectangle(1, 0)

        with self.assertRaises(ValueError):
            r13 = Rectangle(1, 2, -3)

        with self.assertRaises(ValueError):
            r14 = Rectangle(1, 2, 3, -4)

if __name__ == "__main__":
    unittest.main()

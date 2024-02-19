#!/usr/bin/python3
'''Module for Rectangle unit tests.'''
import unittest
import json
import sys

from io import StringIO
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

    def test_area(self):
        """Test the area of rectangle"""
        r1 = Rectangle(1, 2, 3, 4)
        size_area = r1.area()

        self.assertEqual(size_area, 2)

    def test__str__(self):
        """Test __str__"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        expected_output = '[Rectangle] (12) 2/1 - 4/6\n'
    
        original_stdout = sys.stdout
        sys.stdout = StringIO()
    
        print(r1)
        print_output = sys.stdout.getvalue()

        sys.stdout = original_stdout
        self.assertEqual(print_output, expected_output)

    def test_display_without_x_y(self):
        """Test display() whihout x and y"""
        r1 = Rectangle(1, 2)
        expected_output = "#\n#\n"

        original_stdout = sys.stdout
        sys.stdout = StringIO()

        r1.display()
        displayed_output = sys.stdout.getvalue()

        sys.stdout = original_stdout
        self.assertEqual(displayed_output, expected_output)

    def test_display_without_y(self):
        """Test display() whitout y"""
        r1 = Rectangle(1, 2, 1)
        expected_output = " #\n #\n"

        original_stdout = sys.stdout
        sys.stdout = StringIO()

        r1.display()
        displayed_output = sys.stdout.getvalue()

        sys.stdout = original_stdout
        self.assertEqual(displayed_output, expected_output)

    def test_display(self):
        """Test display() whitout y"""
        r1 = Rectangle(1, 2, 1, 1)
        expected_output = "\n #\n #\n"

        original_stdout = sys.stdout
        sys.stdout = StringIO()

        r1.display()
        displayed_output = sys.stdout.getvalue()

        sys.stdout = original_stdout
        self.assertEqual(displayed_output, expected_output)

    def test_to_dictionary(self):
        """Test the distionary"""
        r1 = Rectangle(1, 2, 1, 1, 4)
        expected_output = {'id': 4, 'width': 1, 'height': 2, 'x': 1, 'y': 1}

        dict_1 = Rectangle.to_dictionary(r1)

        self.assertEqual(dict_1, expected_output)

    def test_update_1(self):
        """Test update() in Rectangle"""
        r1 = Rectangle(10, 10, 10, 10)
        expected_output = '[Rectangle] (26) 10/10 - 10/10\n'

        original_stdout = sys.stdout
        sys.stdout = StringIO()
        
        r1.update()
        print(r1)
        update_output = sys.stdout.getvalue()
        
        sys.stdout = original_stdout
        self.assertEqual(update_output, expected_output)

    def test_update_2(self):
        """Test update(89) in Rectangle"""
        r1 = Rectangle(10, 10, 10, 10)
        expected_output = '[Rectangle] (89) 10/10 - 10/10\n'

        original_stdout = sys.stdout
        sys.stdout = StringIO()

        r1.update(89)
        print(r1)
        update_output = sys.stdout.getvalue()

        sys.stdout = original_stdout
        self.assertEqual(update_output, expected_output)

    def test_update_3(self):
        """Test update(89, 1) in Rectangle"""
        r1 = Rectangle(10, 10, 10, 10)
        expected_output = '[Rectangle] (89) 10/10 - 1/10\n'

        original_stdout = sys.stdout
        sys.stdout = StringIO()

        r1.update(89, 1)
        print(r1)
        update_output = sys.stdout.getvalue()

        sys.stdout = original_stdout
        self.assertEqual(update_output, expected_output)

    def test_update_4(self):
        """Test update(89, 1, 2) in Rectangle"""
        r1 = Rectangle(10, 10, 10, 10)
        expected_output = '[Rectangle] (89) 10/10 - 1/2\n'

        original_stdout = sys.stdout
        sys.stdout = StringIO()

        r1.update(89, 1, 2)
        print(r1)
        update_output = sys.stdout.getvalue()

        sys.stdout = original_stdout
        self.assertEqual(update_output, expected_output)

    def test_update_5(self):
        """Test update(89, 1, 2, 3) in Rectangle"""
        r1 = Rectangle(10, 10, 10, 10)
        expected_output = '[Rectangle] (89) 3/10 - 1/2\n'

        original_stdout = sys.stdout
        sys.stdout = StringIO()

        r1.update(89, 1, 2, 3)
        print(r1)
        update_output = sys.stdout.getvalue()

        sys.stdout = original_stdout
        self.assertEqual(update_output, expected_output)

    def test_update_6(self):
        """Test update(89, 1, 2, 3, 4) in Rectangle"""
        r1 = Rectangle(10, 10, 10, 10)
        expected_output = '[Rectangle] (89) 3/4 - 1/2\n'

        original_stdout = sys.stdout
        sys.stdout = StringIO()

        r1.update(89, 1, 2, 3, 4)
        print(r1)
        update_output = sys.stdout.getvalue()

        sys.stdout = original_stdout
        self.assertEqual(update_output, expected_output)

if __name__ == "__main__":
    unittest.main()

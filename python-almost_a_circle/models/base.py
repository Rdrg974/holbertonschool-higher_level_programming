#!/usr/bin/python3
"""A class Base."""
import turtle
import json
import os


class Base:
    """A clase Base."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialise.

        Args:
            id (int): an integer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            json_str = cls.to_json_string([obj.to_dictionary()
                                           for obj in list_objs])
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Function that creates an Object from a JSON file"""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as f:
            json_str = f.read()
            list_dict = cls.from_json_string(json_str)
            return [cls.create(**d) for d in list_dict]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares."""
        turtle.title("Draw")
        turtle.bgcolor("black")
        t = turtle.Turtle()
        t.color("yellow", "red")
        t.shape("turtle")
        t.speed(1)
        for r in list_rectangles:
            t.penup()
            t.goto(r.x, r.y)
            t.pendown()
            t.forward(r.width)
            t.left(90)
            t.forward(r.height)
            t.left(90)
            t.forward(r.width)
            t.left(90)
            t.forward(r.height)
            t.left(90)
        for s in list_squares:
            t.penup()
            t.goto(s.x, s.y)
            t.pendown()
            t.forward(s.size)
            t.left(90)
            t.forward(s.size)
            t.left(90)
            t.forward(s.size)
            t.left(90)
            t.forward(s.size)
            t.left(90)

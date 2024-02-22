#!/usr/bin/python3
"""A class Base."""
import random
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
        if json_string is None or len(json_string) == 0:
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

    def random_color():
        r = random.random()
        g = random.random()
        b = random.random()
        return (r, g, b)
    
    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares."""
        turtle.title("Draw")
        turtle.bgcolor("black")
        t = turtle.Turtle()
        t.shape("turtle")
        t.speed(1)
        for r in list_rectangles:
            t.color(Base.random_color())
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
            t.color(Base.random_color())
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
            
    @staticmethod
    def draw_name(letter):
        """Draw my name"""
        screen = turtle.Screen()
        screen.title("MY NAME")
        screen.bgcolor("Black")
        t = turtle.Turtle()
        t.shape("turtle")
        t.speed(2)
        t.width(3)

        positions = {
        'R': [(-200, 100), (-150, 100), (-150, 50), (-200, 50), (-150, 0)],
        'O': [(-125, 0), (-125, 100), (-75, 100), (-75, 0), (-125, 0)],
        'D': [(-50, 0), (-50, 100), (-35, 100), (0, 75), (0, 25), (-35, 0), (-50, 0)],
        'R2': [(25, 0), (25, 100), (75, 100), (75, 50), (25, 50), (75, 0)],
        'I': [(100, 0), (100, 100), (100, 0)],
        'G': [(125, 0), (125, 100), (175, 100), (125, 100), (125, 0), (175, 0), (175, 50), (165, 50), (175, 50), (175, 0)],
        'U': [(200, 0), (200, 100), (200, 0), (250, 0), (250, 100), (250, 0)],
        'E': [(275, 0), (275, 100), (325, 100), (275, 100), (275, 50), (325, 50), (275, 50), (275, 0), (325, 0)]}
        
        me = {
        'I': [(-200, -50), (-200, -150)]}
        am = {
        'A': [(-150, -150), (-150, -50), (-100, -50), (-100, -100), (-150, -100), (-100, -100), (-100, -150)],
        'M': [(-75, -150), (-75, -50), (-50, -100), (-25, -50), (-25, -150)]}
        sexy = {
        'S': [(25, -50), (25, -100), (75, -100), (75, -150), (25, -150)],
        'E': [(100, -150), (100, -50), (150, -50), (100, -50), (100, -100), (150, -100), (100, -100), (100, -150)],
        'X': [(175, -150), (200, -100), (175, -50), (200, -100), (225, -50), (200, -100), (225, -150)],
        'Y': [(275, -150), (275, -100), (250, -50), (275, -100), (300, -50)]}
        
        coeur = [(-200, -250), (-200, -225), (-191.66, -200), (-183.33, -200), (-175, -225), (-166.66, -200), (-158.33, -200), (-150, -225), (-150, -250), (-175, -300)]
    
        t.penup()
        t.goto(-200, 0)
        t.pendown()
        for pos in positions.values():
            for i in pos:
                t.color(Base.random_color(), Base.random_color())
                t.goto(i)

        t.penup()
        t.goto(-200, -150)
        t.pendown()
        for pos in me.values():
            for i in pos:
                t.color(Base.random_color(), Base.random_color())
                t.goto(i)

        
        t.penup()
        t.goto(-150, -150)
        t.pendown()
        for pos in am.values():
            for i in pos:
                t.color(Base.random_color(), Base.random_color())
                t.goto(i)
                
        t.penup()
        t.goto(75, -50)
        t.pendown()
        for pos in sexy.values():
            for i in pos:
                t.color(Base.random_color(), Base.random_color())
                t.goto(i)
        
        t.penup()
        t.goto(-175, -300)
        t.pendown()
        for pos in coeur:
            t.color(Base.random_color(), Base.random_color())
            t.goto(pos)
        
        t.penup()
        t.goto(-175, -250)
        t.left(90)
        screen.exitonclick()

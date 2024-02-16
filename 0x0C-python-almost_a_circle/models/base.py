#!/usr/bin/python3
"""This module contain the base class"""

import json
import csv


class Base:
    """This class manages id attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ amethod that writes the JSON string
        representation of list_objs to a file"""
        name = cls.__name__ + ".json"
        with open(name, 'w') as myfile:
            if list_objs is None:
                myfile.write("[]")
            else:
                listofdic = [ob.to_dictionary() for ob in list_objs]
                myfile.write(Base.to_json_string(listofdic))

    @staticmethod
    def from_json_string(json_string):
        """ This method returns the list of the JSON str"""
        if json_string is None or not json_string:
            return []
        else:
            thelist = json.loads(json_string)
            return thelist

    @classmethod
    def create(cls, **dictionary):
        """a emthod that returns an instance with all attributes already set"""
        if dictionary and dictionary is not None:
            if cls.__name__ == "Rectangle":
                dummy = cls(5, 6)
            else:
                dummy = cls(8)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """a method that returns a list of instances"""
        name = cls.__name__ + ".json"
        try:
            with open(name, 'r') as myfile:
                content = myfile.read()
            listofdict = Base.from_json_string(content)
            listofinst = [cls.create(**dicty) for dicty in listofdict]
            return listofinst
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file"""
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[
                    o.id, o.width, o.height, o.x, o.y] for o in list_objs]
            else:
                list_objs = [[
                    o.id, o.size, o.x, o.y]for o in list_objs]
        with open(
                '{}.csv'.format(
                    cls.__name__), 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''Loads object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        ret = []
        with open(
                '{}.csv'.format(
                    cls.__name__), 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[
                        1], "height": row[2],
                            "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[
                        1], "x": row[2], "y": row[3]}
                ret.append(cls.create(**d))
        return ret

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module."""
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))
            t.pensize(10)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.end_fill()

        time.sleep(5)

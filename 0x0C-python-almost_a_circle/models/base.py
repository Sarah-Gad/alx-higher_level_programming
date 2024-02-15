#!/usr/bin/python3
"""This module contain the base class"""

import json


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
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items(
                    ))for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module."""
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()
            turt.color("#b5e3d8")
            for sq in list_squares:
                turt.showturtle()
                turt.up()
                turt.goto(sq.x, sq.y)
                turt.down()
                for i in range(2):
                    turt.forward(sq.width)
                    turt.left(90)
                    turt.forward(sq.height)
                    turt.left(90)
                turt.hideturtle()
            turtle.exitonclick()

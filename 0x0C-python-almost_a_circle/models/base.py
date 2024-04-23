#!/usr/bin/python3
""" Base Class """
import json
import csv
import turtle


class Base:
    '''
        Class Name: Base

        Methods :

        Atributes :
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        """ Default Construtor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Json data representation """
        if list_dictionaries is None or list_dictionaries == 0:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Json string to file """
        fileClassJson = cls.__name__ + ".json"
        with open(fileClassJson, "w") as typeJson:
            if list_objs is None:
                return typeJson.write("[]")
            else:
                list_objs = [list_dict.to_dictionary()
                             for list_dict in list_objs]
                typeJson.write(Base.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ Json list reprensation """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Dictionary to Instance """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """ Files to instance """
        refer_file = str(cls.__name__) + ".json"
        try:
            with open(refer_file, "r") as file_json:
                list_dicts = Base.from_json_string(file_json.read())
                return [cls.create(**data) for data in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ write to csv """
        nameOfFile = cls.__name__ + ".csv"
        with open(nameOfFile, "w", newline="") as file_csv:
            if list_objs is None or list_objs == []:
                file_csv.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    names_fields = ["id", "width", "height", "x", "y"]
                else:
                    names_fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(file_csv, fieldnames=names_fields)
                for data in list_objs:
                    writer.writerow(data.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
             Return a list of classes instantiate from a csv.
        """
        name_file = cls.__name__ + ".csv"
        try:
            with open(name_file, "r", newline="") as file_csv:
                if cls.__name__ == "Rectangle":
                    names_field = ["id", "width", "height", "x", "y"]
                else:
                    names_field = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(file_csv, fieldnames=names_field)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
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

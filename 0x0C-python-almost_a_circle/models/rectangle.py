#!/usr/bin/python3

""" importing Base class to child class Rectangle  """
from models.base import Base

class Rectangle(Base):
    """ Rectangle inherits from Parent Class Base """
    def __init__(self, width, height, y=0, x=0, id=None):
        """ Initializer """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def y(self):
        return self.__y

    @property
    def x(self):
        return self.__x

    @width.setter
    def width(self, value):
        self.validating_int("width", value, False)
        self.__width = value

    @height.setter
    def height(self, value):
        self.validating_int("height", value, False)
        self.__height = value

    @y.setter
    def y(self, value):
        self.validating_int("y", value)
        self.__y = value

    @x.setter
    def x(self, value):
        self.validating_int("x", value)
        self.__x = value

    def validating_int(self, name, value, vl=True):
        """ Mehtod calidate value """
        if type(value) != int:
            raise TypeError("{} must bi an integer".format(name))
        if vl and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not vl and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """ Multiply width and height """
        return self.width * self.height

    def display(self):
        """ showstring representation of this rectangle."""
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        '''Returns string info about this rectangle.'''
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''Internal method that updates instance attributes via */**args.'''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updates instance attributes via no-keyword & keyword args.'''
        # print(args, kwargs)
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Returns dictionary representation of this class.'''
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}

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

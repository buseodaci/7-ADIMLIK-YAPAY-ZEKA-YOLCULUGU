# -*- coding: utf-8 -*-
"""
Created on Sat May  2 03:55:35 2020

@author: buse
"""

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

    def toString(self): pass


class Square(Shape):
    "sub class"

    def __init__(self, edge):
        self.__edge = edge

    def area(self):
        result = self.__edge ** 2
        print("Square area: ", result)

    def perimeter(self):
        result = self.__edge * 4
        print("Square perimeter: ", result)

    def toString(self):
        print("Square edge: ", self.__edge)


class Circle(Shape):
    PI = 3.14

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        ""
        result = self.PI * self.__radius ** 2
        print("Circle area: ", result)

    def perimeter(self):
        result = 2 * self.PI * self.__radius
        print("Circle perimeter: ", result)

    def toString(self):
        print("Circle radius: ", self.__radius)


c = Circle(5)
c.area()
c.perimeter()
c.toString()

s = Square(5)
s.area()
s.perimeter()
s.toString()

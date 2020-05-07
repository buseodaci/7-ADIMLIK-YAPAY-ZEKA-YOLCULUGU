# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 01:51:39 2020

@author: buse
"""


# %% calculator
class Calc(object):

    def __init__(self, a, b):
        self.value1 = a
        self.value2 = b

    def add(self):
        return self.value1 + self.value2

    def multiply(self):
        return self.value1 * self.value2

    def division(self):
        return self.value1 / self.value2


selection = input("Choose 1 for add, 2 for multiply, 3 for division = ")
v1 = int(input("first value = "))
v2 = int(input("second value = "))

c1 = Calc(v1, v2)
if selection == "1":
    add_result = c1.add()
    print("Add: {}".format(add_result))
elif selection == "2":
    multiply_result = c1.multiply()
    print("Multiply: {}".format(multiply_result))
elif selection == "3":
    division_result = c1.division()
    print("Division: {}".format(division_result))

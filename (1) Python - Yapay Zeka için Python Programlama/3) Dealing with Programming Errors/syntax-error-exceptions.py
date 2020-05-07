# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 17:00:36 2020

@author: buse
"""

# %% sytntax error
print(8)
# print 8

# %% exceptions
a = 10
b = "2"
liste = [1, 2, 3]
print(sum(liste))
# print(a+b)
print(str(a) + b)
k = 10
print(k)
# print(k/0) #hata
zero = 0
try:
    a = k / zero
except ZeroDivisionError:
    a = 0

# IndexError
list1 = [1, 2, 3, 4]
# list1[15]

# ModuleNotFoundError
# import numpyy
import numpy

# FileNotFoundError
import pandas as pd
# pd.read_csv("asd")

# TypeError
# "2"+2
2 + 2

# ValueError
# int("sad")
int("10")

# finally
try:
    1 / 1
except:
    print("except")
else:
    print("else")
finally:
    print("done")

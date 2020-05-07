# -*- coding: utf-8 -*-
"""
Created on Sat May  2 00:42:27 2020

@author: buse
"""


class Animal:  # parent
    def toString(self):
        print("animal")


class Monkey(Animal):  # child
    def toString(self):
        print("monkey")


animal = Animal()
animal.toString()

monkey = Monkey()
monkey.toString()

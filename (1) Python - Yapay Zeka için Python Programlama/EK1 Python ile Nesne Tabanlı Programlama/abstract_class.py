# -*- coding: utf-8 -*-
"""
Created on Sat May  2 00:17:21 2020

@author: buse
"""

# Abstract classlar; subclasslar için şablon görevi görürler ve kullanılacak ortak fonsiyonları kendi içerisinde tutarlar.
# Abstract classlar instantiate edilemezler.(1.şart)
# Child classlar, abstract classtaki methodları almak zorunda.(2.şart)
# ABC= Abstract Basic Class

from abc import ABC, abstractmethod


# Animal classını nasıl abstract class yapıcaz ?
class Animal(ABC):  # super class
    @abstractmethod
    def walk(self): pass

    @abstractmethod
    def run(self): pass


class Bird(Animal):  # sub class
    def __init__(self):
        print("bird")

    def walk(self):
        print("walk")

    def run(self):
        print("run")


bird = Bird()

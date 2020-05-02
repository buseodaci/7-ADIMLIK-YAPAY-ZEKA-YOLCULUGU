# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 03:28:29 2020

@author: buse
"""


#%% inheritance
class Animal:
    def __init__(self):
        print("animal is created")
        
    def toString(self):
        print("animal")
        
    def walk(self):
        print("animal walk")
        
class Monkey(Animal):
    def __init__(self):
        super().__init__() # use init of parent(animal) class
        print("monkey is created")
        
    def toString(self):
        print("monkey")
        
    def climb(self):
        print("monkey can climb")
        
class Bird(Animal):
    def __init__(self):
        super().__init__()
        print("bird is created")
    
    def fly(self):
        print("bird can fly")
    
    
monkey1=Monkey()
monkey1.toString()
monkey1.walk()
monkey1.climb()
print("------------------")
bird=Bird()
bird.walk()
bird.fly()

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 00:20:24 2020

@author: buse
"""

# %%
#  "#" = ctrl+alt+3
#  "%" = shift+5
integer1 = 33
string = "messi"


# %% classes

class Employee(object):
    # attribute= age,address,name
    # behaviour=pass
    pass  # classımız şu anda boş hata almamak için yazıyoruz, ileride dolduracağımızı ifade ediyor.


employee1 = Employee()


# %% attribute
class Footballer:
    age = 30
    football_club = "barcelona"


f1 = Footballer()
print(f1.football_club)
f1.football_club = "real madrid"
print(f1.football_club)


# %% methods
class Square(object):
    edge = 5

    def area(self):
        area = self.edge * self.edge
        return area


s1 = Square()
print(s1.edge)


# %% methods vs functions
class Emp(object):
    age = 25
    salary = 1000

    def ageToSalaryRatio(self):  # method; belong to class
        print(self.age / self.salary)


emp1 = Emp()
emp1.ageToSalaryRatio()


def ageToSalaryRatio(age, salary):  # function
    a = age / salary
    print("function: ", a)


ageToSalaryRatio(25, 1000)

pi = 3.14


def findArea(a, b):
    area = a * b ** 2
    return area


result1 = findArea(pi, 10)
result2 = findArea(pi, 20)
print(result1 + result2)


# %% initializer or constructor
class Animal(object):
    # name="dog"
    # age=2

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getAge(self):
        return self.age

    def getName(self):
        print(self.name)


# a1=Animal()
# a1_age=a1.getAge()
# print("animal age: ",a1_age)

a2 = Animal("dog", 2)
a3 = Animal("cat", 4)
a4 = Animal("bird", 6)

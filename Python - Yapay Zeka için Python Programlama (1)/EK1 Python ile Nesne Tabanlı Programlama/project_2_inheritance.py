# -*- coding: utf-8 -*-
"""
Created on Fri May  1 23:38:18 2020

@author: buse
"""


class Website:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def loginInfo(self):
        print(self.name + " " + self.surname)


class Website2(Website):
    def __init__(self, name, surname, ids):
        Website.__init__(self, name, surname)
        self.ids = ids

    def login(self):
        print(self.name + " " + self.surname + " " + self.ids)


class Website3(Website):
    def __init__(self, name, surname, email):
        Website.__init__(self, name, surname)
        self.email = email

    def login(self):
        print(self.name + " " + self.surname + " " + self.email)


def login(self):
    print(self.name + " " + self.surname + " " + self.email)


person = Website("name", "surname")
person2 = Website2("name", "surname", "123")
person3 = Website3("name", "surname", "email@gmail.com")

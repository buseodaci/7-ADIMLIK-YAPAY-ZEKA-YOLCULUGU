# -*- coding: utf-8 -*-
"""
Created on Sat May  2 03:46:07 2020

@author: buse
"""


class Employee:
    def raisee(self):
        raise_rate = 0.1
        return 100 + 100 * raise_rate


class CompEng(Employee):
    def raisee(self):
        raise_rate = 0.2
        return 100 + 100 * raise_rate


class EEE(Employee):
    def raisee(self):
        raise_rate = 0.3
        return 100 + 100 * raise_rate


e1 = Employee()
ce = CompEng()
eee = EEE()

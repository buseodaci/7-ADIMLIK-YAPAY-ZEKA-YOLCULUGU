# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 02:54:49 2020

@author: buse
"""


# %% encapsulation
class BankAccount(object):
    def __init__(self, name, money, address):
        self.name = name  # global
        self.__money = money  # private
        self.address = address

    def getMoney(self):
        return self.__money

    def setMoney(self, amount):
        self.__money = amount

    def __increase(self):  # private method
        self.__money = self.__money + 500


p1 = BankAccount("messi", 1000, "barcelona")
p2 = BankAccount("neymar", 2000, "paris")

print("get method : ", p1.getMoney())
p1.setMoney(3000)
print("set method : ", 5000)
# =============================================================================
# p1.increase()
# print("after raise : ",p1.getMoney())
# 
# =============================================================================

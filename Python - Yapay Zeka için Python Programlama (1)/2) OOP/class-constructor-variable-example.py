# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:37:22 2020

@author: buse
"""

# %% class, constructor
class Calisan:
    zamOrani = 1.8
    counter = 0

    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + soyisim + "@asd.com"
        Calisan.counter = Calisan.counter + 1

    def giveNameSurname(self):
        return self.isim + " " + self.soyisim

    def zamYap(self):
        self.maas = self.maas + self.maas * self.zamOrani


calisan = Calisan("ali", "veli", 100)
print(calisan.giveNameSurname())

# %% class variables
print(Calisan.counter)
print("ilk maas: ", calisan.maas)
calisan.zamYap();
print("ilk maas: ", calisan.maas)
calisan2 = Calisan("ayse", "veli", 200)
print(Calisan.counter)

# %% class example
calisan3 = Calisan("eren", "veli", 400)
calisan4 = Calisan("yelda", "ahmet", 600)
calisan5 = Calisan("kısmet", "uçak", 800)
liste = [calisan, calisan2, calisan3, calisan4, calisan5]

max_maas = -1
index = -1
for each in liste:
    if each.maas > max_maas:
        max_maas = each.maas
        index = each
print(max_maas)
print(index.giveNameSurname())

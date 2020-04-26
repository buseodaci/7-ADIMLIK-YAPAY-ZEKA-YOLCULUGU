# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:24:12 2020

@author: buse
"""

# %% list
liste = [1, 2, 3, 4, 5, 6]
# type(liste)
liste_str = ["ptesi", "sali", "cars"]
value = liste[1]
print(value)
last_value = liste[-1]
liste_divide = liste[0:3]
# dir(liste)
# help(list.append)
liste.append(7)
liste.remove(7)
liste.reverse()
liste2 = [3, 5, 1, 2, 6]
liste2.sort()

# %% tuple
t = (1, 2, 3, 4, 5, 6)
t.count(3)
t.index(3)

# %% dictionary
# küçük bir db oluşturmak istersek veya multiple değer döndürmek istediğimizde kullanabiliriz.
dictionary = {"ali": 32, "veli": 45, "ayse": 13}
dictionary["ali"]
type(dictionary["ali"])
dictionary.keys()
# dict_keys(['ali', 'veli', 'ayse'])
dictionary.values()


# dict_values([32, 45, 13])
def deneme():
    dictionary = {"ali": 32, "veli": 45, "ayse": 13}
    return dictionary


dic = deneme()
dic["veli"]

# %% conditionals
var1 = 10
var2 = 20

if (var1 > var2):
    print("var1 buyuktur var2")
elif (var1 == var2):
    print("var1 ve var2 eşitler")
else:
    print("var1 kucuktur var2")

liste = [1, 2, 3, 4, 5]
value = 3
if value in liste:
    print("evet {} degeri listenin icinde".format(value))
else:
    print("hayir")

keys = dictionary.keys()
if "can" in keys:
    print("Evet")
else:
    print("hayir")


# %% QUIZ 2

def yuzyil_dondur(yil):
    yil_str = str(yil)
    if (len(yil_str) < 3):
        return 1
    elif (len(yil_str) == 3):
        if (yil_str[1:3] == "00"):
            return int(yil_str[0])
        else:
            return int(yil_str[0]) + 1
    else:
        if (yil_str[2:4] == "00"):
            return int(yil_str[:2])
        else:
            return int(yil_str[:2]) + 1


yuzyil_dondur(2005)

# %% loops
# for
for each in range(1, 11):
    print(each)
for each in "ankara ist":
    print(each)

for each in "ankara ist".split():
    print(each)

liste = [1, 4, 5, 6, 32, 7, 3]
summation = sum(liste)

sum_liste = 0
for each in liste:
    sum_liste = sum_liste + each
    print(sum_liste)

# while
i = 0
while (i < 4):
    print(i)
    i = i + 1

sinir = len(liste)
each = 0
count = 0
while (each < sinir):
    count = count + liste[each]
    each = each + 1

# %% QUIZ 3
liste = [1, 2, 3, 4, 5, 6, 4, 23, 67, 21, -500, 23, 451, 67]
en_kucuk = 0;
for i in liste:
    if (i < en_kucuk):
        en_kucuk = i

print(en_kucuk)

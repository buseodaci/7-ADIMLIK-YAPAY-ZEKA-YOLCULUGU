# -*- coding: utf-8 -*-

# %% variable
var1 = 10
var2 = 15
gun = "pazartesi"
var3 = 10.0
# 4var=10 # yanlış

# %% string
s = "bugun gunlerden pazartesi"
variable_type = type(s)
print(s)
var1 = "ankara"
var2 = "ist"
var3 = var1 + var2
var4 = "100"
var5 = "200"
var6 = var4 + var5
uzunluk = len(var6)
print(var6[0])

# %% numbers
integer_deneme = -50
float_deneme = -40.5

# %% built in functions
str1 = "deneme"
float1 = 10.6
# float(10)
# int(float1)
# round(float1)
str2 = "1000"
# int(str2)

# %% user defined functions
var1 = 20
var2 = 50
output = (((var1 + var2) * 50) / 100.0) * var1 / var2


def first_function(a, b):
    output = (((a + b) * 50) / 100.0) * a / b
    return output


result = first_function(var1, var2)


# %% default and flexible functions

# default
def cember_cevresi_hesapla(r, pi=3.14):
    output = 2 * pi * r
    return output


# flexible
def hesapla(boy, kilo, *args):
    print(len(args))
    output = (boy + kilo) * args[0]
    return output


# %% QUIZ
yas = 10
isim = "ali"
soyisim = "veli"


def function_quiz(yas, isim, *args, ayakkabi_numarasi=35):
    print("Cocugun ismi: ", isim, " yasi: ", yas, " ayak numarasi: ", ayakkabi_numarasi)
    print(float(yas))
    output = args[0] * yas
    return output


sonuc = function_quiz(yas, isim, soyisim)


# %% lambda
def hesaplaKare(x):
    return x * x


sonuc = hesapla(3)
print(sonuc)
sonuc2 = lambda x: x * x
print(sonuc2(3))

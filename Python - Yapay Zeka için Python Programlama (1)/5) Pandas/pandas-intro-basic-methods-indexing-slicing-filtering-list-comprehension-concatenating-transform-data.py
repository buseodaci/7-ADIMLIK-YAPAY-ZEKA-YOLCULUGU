# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 04:34:34 2020

@author: buse
"""

# %% introduction to pandas
# =============================================================================
# *numpy array lerle yapılan işlemlerde ve depolamada kullanılırken, pandas dataframeler için oluşturulmuş kütüphanedir.
# 1) pandas hizli ve etkili for dataframes
# 2) csv ve text dosyalarına acip inceleyip sonuclarimiza bu dosya tiplerine rahat bir sekilde kaydedebilir.(Dosyalar arası geçiş hızlıdır)
# 3) missing data için işimizi kolaylaştırıyor.
# 4) reshape yapıp datayı daha etkili bir şekilde kullanabiliriz.
# 5) slicing, indexing kolay
# 6) time series data analizinde çok yardımcı
# 7)  optimize edilmiş, hızlı bir kütüphane.
# =============================================================================

import pandas as pd

# dataframe nasıl oluşturulur? 
dictionary = {"NAME": ["ali", "veli", "kenan", "hilal", "ayse", "evren"],
              "AGE": [15, 16, 17, 33, 45, 66],
              "MAAS": [100, 150, 240, 350, 110, 220]
              }

dataFrame1 = pd.DataFrame(dictionary)
head = dataFrame1.head()  # ilk 5 sample ı verir(5 yerine custom data sayısı da verilebilir)
head2 = dataFrame1.head(6)
tail = dataFrame1.tail()  # son 5 sample,bu özellikleri veri önincelemesinde kullanabiliriz.

# %% pandas basic method
print(dataFrame1.columns)
print(dataFrame1.info())  # Dtype; object =string
print(dataFrame1.dtypes)
print(dataFrame1.describe())  # numeric feature= columns(age,maas)

# %% indexing and slicing
print(dataFrame1["NAME"])
print(dataFrame1["AGE"])  # AGE  verisini çekmenin 1. yolu
print(dataFrame1.loc[:, "AGE"])  # 2.yolu
print(dataFrame1.AGE)  # 3.yolu
dataFrame1["yeni feature"] = [-2, -3, -1, -5, -4, -6]  # feature oluştururken boşluk bırakma camelCase ya da "_" kullan.
# dataFrame1.yeni feature #yoksa bu şekilde feature çağıramayız.
print(dataFrame1.loc[0:3, "AGE"])
print(
    dataFrame1.loc[0:3, "AGE":"yeni feature"])  # 2 feature arasında bütün verilerin 0:3 arasındaki sample ı getirecek.
print(dataFrame1.loc[0:3, ["AGE", "yeni feature"]])
print(dataFrame1.loc[::-1, :])  # reverse
print(dataFrame1.loc[:, :"NAME"])  # NAME' e kadar olan satırları yazdır.
print(dataFrame1.loc[:, "NAME"])  # loc= location
print(dataFrame1.iloc[:, 2])  # iloc=interger location, yani index(columnların indexi) yazmamız gerek. -NAME =2-

# %% filtering
filtre1 = dataFrame1.MAAS > 200
print(filtre1)  # bu şekilde ilk series imizi elde etmiş olduk.
filtrelenmisData = dataFrame1[filtre1]
filtre2 = dataFrame1.AGE < 20
dataFrame1[filtre1 & filtre2]
print(dataFrame1[dataFrame1.AGE > 60])

# %% list comprehension
import numpy as np

ortalama_maas = dataFrame1.MAAS.mean()
# ortalama_maas_numpy=np.mean(dataFrame1.MAAS) # numpy ile ortalama maaş hesabı
dataFrame1["maas_seviyesi"] = ["dusuk" if ortalama_maas > each else "yuksek" for each in dataFrame1.MAAS]

# =============================================================================
# for each in dataFrame1.MAAS:
#     if(ortalama_maas>each):
#         print("dusuk")
#     else:
#         print("yuksek")
# 
# 
# =============================================================================

dataFrame1.columns = [each.lower() for each in dataFrame1.columns]
dataFrame1.columns = [each.split()[0] + "_" + each.split()[1] if (len(each.split()) > 1) else each for each in
                      dataFrame1.columns]

# %% drop and concatenating 
# axis=0 ile soldan sağa(row) drop ediyoruz.
# axis=1 ile yukarıdan aşağıya(column u) drop ediyoruz.
# implace=True ile feature drop edildikten sonra dataFrame1 'i güncelle.
dataFrame1.drop(["yeni_feature"], axis=1, inplace=True)

data1 = dataFrame1.head()
data2 = dataFrame1.tail()
# vertical, satırları birleştir.
data_concat = pd.concat([data1, data2], axis=0)

# horizontal, kolonları birleştir.
maas = dataFrame1.maas
age = dataFrame1.age
data_horizontal_concat = pd.concat([maas, age], axis=1)

# %% transforming data
# 1.yol
dataFrame1["list_comprehension"] = [each * 2 for each in dataFrame1.age]

# 2.yol
def multiply(age):
    return age * 2

dataFrame1["apply_metodu"] = dataFrame1.age.apply(multiply)

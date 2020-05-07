# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:00:41 2020

@author: buse
"""

# %% pandas review
# matplotlib : görsellestirme kutuphanesi
# line plot,scatter plot, bar plot, subplots,histogram

import pandas as pd

df = pd.read_csv("iris.csv")

# kaç farklı cicek var ?
print(df.Species.unique())
print(df.info())
# describe(): string olmayan numerik degerleri karşılaştırmamızı sağlıyor
print(df.describe())

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]
print(setosa.describe())
print(versicolor.describe())

# %% matplotlib, line plot
import matplotlib.pyplot as plt

df1 = df.drop(["Id"], axis=1)

# defaultda line plot var
# df1.plot()
# plt.show()

plt.plot(setosa.Id, setosa.PetalLengthCm, color="red", label="setosa")
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color="green", label="versicolor")
plt.plot(virginica.Id, virginica.PetalLengthCm, color="blue", label="virginica")
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()  # label ların yazılmasını sağlıyor 
plt.title("line plot")
plt.show()

# df1.plot(grid=True,lineStyle=":")
df1.plot(grid=True, alpha=0.5)  # alpha, saydamlık arttıran feature
plt.show()

# %% scatter plot
# 2 feature i karsilastirmak icin kullanilir.
setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.scatter(setosa.PetalLengthCm, setosa.PetalWidthCm, c="red", label="setosa")
plt.scatter(versicolor.PetalLengthCm, versicolor.PetalWidthCm, c="green", label="versicolor")
plt.scatter(virginica.PetalLengthCm, virginica.PetalWidthCm, c="blue", label="virginica")
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.legend()
plt.title("scatter plot")
plt.show()

# %% histogram
# frekans sıklıgı
plt.hist(setosa.PetalLengthCm, bins=40)
plt.xlabel("PetalLengthCm degerleri")
plt.ylabel("frekans")
plt.title("histogram")
plt.show()

# %% bar plot
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7])
y = x * 2 + 5
plt.bar(x, y)
plt.title("bar plot")
plt.xlabel("x")
plt.label("y")
plt.show()

# %% subplot
# aynı framede farklı plotları çizdirmesi demek.
df1.plot(grid=True, alpha=0.5, subplots=True)
plt.subplot(3, 1, 1)
plt.plot(setosa.Id, setosa.PetalLengthCm, color="red", label="setosa")
plt.subplot(3, 1, 2)
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color="green", label="versicolor")
plt.subplot(3, 1, 3)
plt.plot(virginica.Id, virginica.PetalLengthCm, color="blue", label="virginica")
plt.show()

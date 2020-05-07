# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 23:09:02 2020

@author: buse
"""

# %% numpy basics
import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
print(array.shape)
a = array.reshape(3, 5)
print("shape: ", a.shape)
print("dimension: ", a.ndim)
print("data type: ", a.dtype.name)
print("size: ", a.size)
print("type: ", type(a))
array1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 5]])
zeros = np.zeros((3, 4))
zeros[0, 0] = 5
print(zeros)
np.ones((3, 4))
np.empty((2, 3))
a = np.arange(10, 50, 5)
print(a)
b = np.linspace(1, 5, 10)
print(b)

# %% numpy basic operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)
print(a - b)
print(a ** 2)
print(np.sin(a))
print(a < 2)

c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[1, 2, 3], [4, 5, 6]])
# element wise product
print(c * d)

# matrix product
print(c.dot(d.T))
print(np.exp(c))
e = np.random.random((5, 5))
print(e)
print(e.sum())
print(e.max())
print(e.min())

# matrix satir değerlerini toplama
print(e.sum(axis=1))

# matrix column değerlerini toplama
print(e.sum(axis=0))

print(np.sqrt(a))
print(np.square(a))

# %% indexing and slicing
array = np.array([1, 2, 3, 4, 5, 6, 7])
print(array[0:4])
reverse_array = array[::-1]

array1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(array1[1, 1])
print(array1[:, 1])  # 1. column
print(array1[1, 1:4])
print(array1[-1, :])  # last row
print(array1[:, -1])  # last column

# %% shape manipulation
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array_ravel = array.ravel()
array2 = array_ravel.reshape(3, 3)
arrayT = array2.T
print(arrayT.shape)
# reshape vs resize farkı: ikisi de matrix in boyutunu değiştiriyor fakat resize kullandığımızda orjinal matrixi 
# değiştirirken, reshape de ise işlem sonrası yeni bir array e atamak zorundayız değişimi görebilmek için.

# %% stacking arrays
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[-1, -2], [-3, -4]])

# vertical 
# array([[1, 2],
#       [3, 4]
#       [-1, -2],
#       [-3, -4]])

array3 = np.vstack((array1, array2))

# horizontal
# array([[1, 2],[-1, -2],
#       [3, 4],[-3, -4]])

array4 = np.hstack((array1, array2))

# %% convert and copy
liste = [1, 2, 3, 4]  # list
array = np.array(liste)  # list to array
liste2 = list(array)  # array to list
a = np.array([1, 2, 3])
b = a
c = a
# bu şekilde tanımladığımız takdirde b veya c arraylerinde herhangi bir güncellemede diğer 2 array de guncellenecektir
# ki biz bunu istemiyoruz. Bunu çözebilmek için de eşitlemek yerine elimizdeki arrayin kopyasını b ve c array lerine
# veriyoruz.
d = np.array([1, 2, 3])
e = d.copy()
f = d.copy()

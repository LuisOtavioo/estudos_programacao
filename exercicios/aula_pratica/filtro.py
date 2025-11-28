import numpy as np

#a é uma matriz de inteiros.
a = np.array([[1,2,3],[4,5,6]])
print(a)

print('indices de elementos <4')

b = np.where(a<4)
print(b)


print("Elementos que são < 4")
print(a[a<4])
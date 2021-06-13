# HackerRank Unir filas y columnas de varias matrices con concatenate
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([7, 8, 9])

resultado = np.concatenate((arr1, arr2, arr3))
print(resultado)

print()

arr4 = np.array([[1, 2, 3], [4, 5, 6]])
arr5 = np.array([[7, 8, 9], [10, 11, 12]])

resultado2 = np.concatenate((arr4, arr5), axis=1) # cuando es una matriz bidimensional se especifica del eje
resultado3 = np.concatenate((arr4, arr5), axis=0)
print(resultado2)
print('\n',resultado3, resultado3.shape)

# Ejercicio

n, m, p = tuple(map(int, input().split()))

matriz1 = []
matriz2 = []
for _ in range(n):
    matriz1.append(list(map(int, input().split())))
    
for _ in range(m):
    matriz2.append(list(map(int, input().split())))

matriz_concatenada = np.concatenate((matriz1, matriz2), axis=0) # el eje0 es el por defecto, no es necesario   especificarlo
print(matriz_concatenada)
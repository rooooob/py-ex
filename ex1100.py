# 1100 HackerRank Obtener la traspuesta y la version aplanada de una matriz numpy

import numpy as np

matriz = np.array([[1, 2, 3], [4, 5, 6]])
matriz_traspuesta = np.transpose(matriz)

print(matriz_traspuesta)
print(matriz_traspuesta.shape)

# 
print('\nUso de flatten')
matriz_aplanada = matriz.flatten() # nos devuelve una matriz de n elementos x 1
print(matriz_aplanada)
print(matriz_aplanada.shape)

# Ejercicio

if __name__ == '__main__':
    n, m = tuple(map(int, input().split())) # n x m dimensiones de la matriz
    
    matriz_i = []
    for _ in range(n):
        matriz_i.append(list(map(int, input().split())))
    
    matriz_i = np.array(matriz_i)

    print(np.transpose(matriz_i))
    print(matriz_i.flatten())


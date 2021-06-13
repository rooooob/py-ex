# Crear una matriz identica con la funcion identity
import numpy as np

print(np.identity(3)) # crea una matriz identica 3x3

# 
print('eye')

print(np.eye(8, 7, k=2)) # eye(r, c, k) k es la diagonal donde seran 1 los valores, si es negativa sera una diagonal inferior

# Ejercicio
print('')
if __name__ == '__main__':
    np.set_printoptions(legacy='1.13')

    rows, columns =  tuple(map(int, input().split()))

    print(np.eye(rows, columns, k=0 ))
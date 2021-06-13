# Usar las funciones floor, ceil y rint sobre un arreglo numpy
import numpy as np

arr = np.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])

print('floor')
print(np.floor(arr))

print('ceil')
print(np.ceil(arr))

print('rint')
print(np.rint(arr))

# Ejercicio
if __name__ == '__main__':
    np.set_printoptions(legacy='1.13')

    matrix = list(map(float, input().split()))
    
    a = np.array(matrix)

    print(np.floor(a))
    print(np.ceil(a))
    print(np.rint(a))
# Funciones min y max en numpy
import numpy as np

arr = np.array([[2, 5], [3, 7], [1, 3], [4, 0]])

print(arr, '\n')
print(np.min(arr, axis=0)) # devuelve el valor minimo de un eje dado
print(np.min(arr, axis=1)) 
print(np.min(arr, axis=None)) # este es el parametro por defecto

print()

print(np.max(arr, axis=0)) 
print(np.max(arr, axis=1))
print(np.max(arr))

# Ejercicio
if __name__ == '__main__':
    n, m = tuple(map(int, input().split()))

    myarr = []
    for _ in range(n):
        myarr.append(list(map(int, input().split())))
    
    mynp = np.array(myarr)
    min_axis1 = np.min(myarr, axis=1)
    print(min_axis1)
    print(np.max(min_axis1))


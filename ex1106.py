# Calcular el promedio, varianza y desviacion estandar
import numpy as np

arr = np.array([[1, 2], [3, 4]])

print(np.mean(arr, axis=0)) # promedio en el eje x (1+3)/2, (2+4)/2
print(np.mean(arr, axis=1)) # promedio en el eje y  (1+2)/2, (3+4)/2
print(np.mean(arr, axis=None))  # (1+2+3+4)/4

print()
print(np.var(arr, axis=0)) # varianza eje x
print(np.var(arr, axis=1)) # varianza eje x
print(np.var(arr, axis=None)) 

print()
print(np.std(arr, axis=0)) # desviacion estandar x
print(np.std(arr, axis=1)) # desviacaion estandar y
print(np.std(arr, axis=None)) 
print()

# Ejercicio
if __name__ == '__main__':
    m, n = tuple(map(int, input().split()))

    mtx = []

    for _ in range(n):
        mtx.append(list(map(int, input().split())))
    
    arr_e = np.array(mtx)

    print(np.mean(arr_e, axis=1))
    print(np.var(arr_e, axis=0))
    print(np.std(arr_e))
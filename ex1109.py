# Calcular la suma y el producto por filas y columnas de una matriz
import numpy as np

my_array = np.array([
    [1, 2],
    [3, 4]
])

print(np.sum(my_array, axis=0))
print(np.sum(my_array, axis=1))
print(np.sum(my_array, axis=None))

print()
print(np.prod(my_array, axis=0))
print(np.prod(my_array, axis=1))
print(np.prod(my_array, axis=None))

# Ejercicio
if __name__ == '__main__':
    n, m = tuple(map(int, input().split()))

    my_list = []

    for _ in range(n):
        my_list.append(list(map(int, input().split())))

    arr = np.array(my_list)

    suma_axis0 = np.sum(arr, axis=0)
    print(np.prod(suma_axis0))
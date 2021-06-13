# Calcular el producto interno y externo entre dos matrices
import numpy as np

arr1 = np.array([0, 1])
arr2 = np.array([3, 4])

print(np.inner(arr1, arr2)) # 0x3 + 1x4 = 4

print(np.outer(arr1, arr2)) # 0x[3, 4] 1x[3, 4] [[0, 0], [3, 4]]


# Ejercicio
if __name__ == '__main__':
    first_arr = list(map(int, input().split()))
    second_arr = list(map(int, input().split()))

    print(np.inner('\n',first_arr, second_arr))
    print(np.outer(first_arr, second_arr))

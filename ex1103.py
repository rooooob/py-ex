# 1103 Multiplicacion de matrices con matmult
import numpy as np

arr1 = np.array([1, 2], dtype='int8')
arr2 = np.array([3, 4], dtype='int8')

dot_prod = np.dot(arr1, arr2) # 2x3 + 2x4 = 11
print(dot_prod)

print()

cross_prod = np.cross(arr1, arr2) # 1x4 - 2x3 = -6 
print(cross_prod)

# Ejercicio

if __name__ == '__main__':
    n = int(input())

    mtx1 = []
    mtx2 = []

    for _ in range(n):
        mtx1.append(list(map(int, input().split())))

    for _ in range(n):
        mtx2.append(list(map(int, input().split())))
    
    print('\n', np.matmul(mtx1, mtx2))
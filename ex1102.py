# 1102 Generar matrices Zeros y Ones
import numpy as np

zero22 = np.zeros((2, 2)) # por defecto el tipo de datos es float32
zero35 = np.zeros((3, 5), dtype='int8')

print(zero35)

one23 = np.ones((2, 3), dtype='int8')
print('\n', one23)

# Ejercicio
if __name__ == '__main__':
    n, m, r = tuple(map(int, input().split()))
    
    zeros = np.zeros((n, m), dtype='int8')
    ones = np.ones((n, m), dtype='int8')
    
    for _ in range(r):
        print(zeros, '\n')
    
    for _ in range(r):
        print(ones, '\n')
# Calculo del determinante de una matriz, valores propios y la inversa
import numpy as np

arr = [[1, 2], [2, 1]]
print(np.linalg.det(arr))

print()

vals, vecs = np.linalg.eig(arr) # valores propios (eigenvectors)
print(vals)
print(vecs)

print()

multiplicative = np.linalg.inv(arr) # la inversa de la matriz
print(multiplicative)

print()
# Ejercicio
# Halle el determinante de la matriz con una precision de 2 decimales
# La primera linea de entrada contiene las dimensiones de la matriz cuadrada  
# Las siguientes lineas contienen los elementos de la matriz separados por espacio

if __name__ == '__main__':
    dim = int(input())

    arr1 = []

    for _ in range(dim):
        arr1.append(tuple((map(float, input().split()))))
    
    matrix = np.array(arr1, dtype='float32')

    determinante = np.linalg.det(matrix)
    print(determinante)
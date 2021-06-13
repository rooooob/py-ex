# Operaciones aritmeticas esenciales sobre arreglos 
import numpy as np 

a = np.array([1, 2, 3, 4], dtype='float32')
b = np.array([5, 6, 7, 8], dtype='float32')

print('Adicion')
print(a+b)
print(np.add(a, b))

print('Substraccion')
print(a-b)
print(np.subtract(a, b))

# podemos aplicar todas estas operaciones basicas como en los arreglos normales
print('Multiplicacion')
print(np.multiply(a, b))
print('Division')
print(np.divide(a, b))
print('Modulo')
print(np.mod(a, b))
print('Potencia')
print(np.power(a, b))

# Ejercicio

if __name__ == '__main__':
    print('Ejercicio')
    r , c = tuple(map(int, input().split()))

    ls_a = []
    ls_b = []

    for _ in range(r):
        ls_a.append(list(map(int, input().split())))
    
    for _ in range(r):
        ls_b.append(list(map(int, input().split())))

    arr_a = np.array(ls_a)
    arr_b = np.array(ls_b)

    print(np.multiply(a, b))
    print(np.power(a, b))
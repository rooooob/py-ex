# Calcular el valor de un polinomio evaluando en un valor x
import numpy as np

# retorna los coheficientes de un polinomio con la secuencia de raices dadas
print(np.poly([-1, 1, 1, 10]))

# root - retorna los valores de las raices de un polinomio dados los coheficientes
print(np.roots([1, 0, -1]))

# polinit - retorna la antiderivada (integral indefinida) de un polinomio
print(np.polyint([1, 1, 1]))

# polider - retorna la derivada de el orden especificado de un polinomio
print(np.polyder([1, 1, 1, 1]))

# polyvar - evalua el polinomio en el valor especificado
print(np.polyval([1, -2, 0, 4], 4))

# polyfit - fits a polynomial of a specified order to a set of data using a least-squares approach
print(np.polyfit([0, 1, -1, 2, -2], [0, 1, 1, 4, 4], 2))

# Ejercicio
print()

if __name__ == '__main__':
    coefficients = list(map(float, input().split()))    
    x = float(input())

    print(np.polyval(coefficients, x))
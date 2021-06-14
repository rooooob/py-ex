# 1001 Ordenar una lista de numeros a partir del modulo calculado por cada numero

# [101, 203, 105, 100, 53]  
# [1, 3, 0, 0, 3] => modulo entre la longitud del array (5)
# [105, 100, 101, 203, 53] => lista ordenada

lista = [101, 203, 105, 100, 53]

lista_ascendente  = sorted(lista, key=lambda x: x % len(lista))
lista_descendente = sorted(lista, key=lambda x: x % len(lista), reverse=True)
print('Ex 1001')
print(lista_ascendente, lista_descendente)

# 1002 Extraer las vocales minusculas de un texto usando la funcion filter
texto = 'Python Es Tremendo'

print('Ex 1002')
vocales_minusculas = list(filter(lambda x: True if x in 'aeiou' else False, texto))
print(vocales_minusculas)

# 1003 Extraer las consonantes mayusculas desde un texto usando la funcion filter
frase = 'PythoN es TrEMeNdO'

print('Ex 1003')
consonantes_mayusculas = list(filter(lambda c: True if c.lower() not in 'aeiou' and c.isupper()  else False, frase))
print(consonantes_mayusculas)

# 1005 Extraer las consonantes minuscula de un texto usando filter
from string import ascii_lowercase

print('Ex 1005')
cons_minusculas = set(ascii_lowercase) - set('aeiou')

consonantes_minusculas = list(filter(lambda c: c in cons_minusculas, texto))
print(consonantes_minusculas)

# 1006 Extraer los digitos que se hallen en un texto usando la funcion filter

print('Ex 10006')
frase2 = 'El año actual es 2021'

digitos = list(map(lambda n: int(n), list(filter(lambda n: n in '0123456789', frase2))))
print(digitos)

# test commit
import matplotlib.pyplot as plt
import numpy as np

weeks = np.array(['w1', 'w2', 'w3', 'w4', 'w5'])
hours = np.array([11.4, 10.6, 13.3, 9.2, 14.2])

plt.plot(weeks, hours)
plt.show()

# comentario desde github

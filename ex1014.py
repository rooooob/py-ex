# 1014 Usar una expresion lambda para ordenar una lista de cadenas a partir de un segundo caracter
print('Ex 1014')

lenguajes = ['Pyhton', 'Javascript', 'C#', 'Go', 'PHP', 'Java']

resultado = sorted(lenguajes, key=lambda c: c[1])
print(resultado)

# 1015 Ordenar una lista de tuplas a partir del segundo elemento de cada tupla
print('Ex 1015')

datos = [(1003, 'Desktop Clone'), (1004, 'Gamer Portatil'), (1002, 'Tablet'), (1003, 'Apple MacBook')]
datos_ordenados = sorted(datos, key=lambda e: e[1])
print(datos_ordenados)

# 1016 Ordenar una lista de tuplas a partir del ultimo caracter del segundo elemento
print('Ex 1016')

datos_ord2 = sorted(datos, key=lambda e: e[-1][-1])
print(datos_ord2)

# 1017 Usar map para concatenar texto de forma masiva a una lista de cadenas de caracteres
print('Ex 1017')

nombres = ['Alexandr', 'Vladimir', 'Ana', 'Ivan', 'Mikhail', 'Nikolai']    

prs = list(map(lambda c: f'{c}ovich', nombres))
print(prs)

# 1018 Obtener la longitud de cada cadena de texto de una lista usando map
print('Ex 1018')

l_cada_nombre = list(map(lambda n: len(n), nombres))
print(l_cada_nombre)

# 1019 Sumar elemento a elemento los datos de dos listas usando map
print('Ex 1019')

numeros1 = [1, 2, 3, 4, 5]
numeros2 = [6, 7, 8, 9, 10]

res = list(map(lambda x, y: x+y, numeros1, numeros2))
print(res)

# 1020 Multiplicar elemento a elemento los datos de dos listas usando map
print('Ex 2020')

res_m = list(map(lambda x, y: x * y, numeros1, numeros2))
print(res_m)
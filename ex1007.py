# 1007 Tomar los valores menores a 100 de una lista y luego sumar a cada uno 10 unidades

numeros = [150, 250, 183, 50, 10, 330, 25, 67]

print('Ex 1007')

menores_plus10 = [x + 10 for x in numeros if x < 100]
menores_plus10fm = list(map(lambda n: n + 10, filter(lambda n: n < 100, numeros)))
print(menores_plus10)
print(menores_plus10fm)

# 1008 Invertir el signo de los numeros de una lista  y luego tomar aquellos mayores a 100

print('Ex 1008')
numeros2 = [-150, 50, 80, -1000, -20, 2, 3]

invertidos_m100 = list(filter(lambda x: x > 100, map(lambda x: x *(-1), numeros2)))
print(invertidos_m100)

# 1009 Usar zip para fusionar dos listas de elementos relacionados
print('Ex 1009')

lenguajes = ['Python', 'Java', 'C#', 'Javascript']
versiones = ['3.10.2', '15', '9', 'ES6']

fusion = list(zip(lenguajes, versiones))
print(fusion)

# 1010 Usar zip para fusionar dos listas en un diccionario
print('Ex 1010')

fusion_dicc = dict(zip(lenguajes, versiones))
print(fusion_dicc)

# 1011 Ordenar con sorted el resultado de fusionar 
print('Ex 1011')
sorted(fusion)

# 1012 Definir las operaciones aritmeticas basicas usando expresiones lambda
print('Ex 1012')

sumar = lambda x, y: x + y
restar = lambda x, y: x - y
multiplicar = lambda x , y: x * y
dividir = lambda x, y: x / y

# 1013 Ordenar una lista con sort y una funcion lambda como llave de ordenamiento
print('Ex 1013')

nrs = [13, 2, 19, 5, 7, 11, 17]
nrs.sort(key=lambda x: x % 2)
print(nrs)
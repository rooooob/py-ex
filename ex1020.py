# 1020 Multiplicar elemento a elemento los datos de dos listas usando map
numeros1 = [1, 2, 3, 4, 5]
numeros2 = [6, 7, 8, 9, 10]

resultado = list(map(lambda x, y: x * y, numeros1, numeros2))
print(resultado)

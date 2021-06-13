# Sumar elemento a elemento los datos de dos lista usando map()

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

resultado = list(map(lambda x, y: x + y, l1, l2))
print(resultado)
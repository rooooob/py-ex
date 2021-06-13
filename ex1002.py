# Extraer las vocales minusculas de un texto usando filter
frase = 'Python es Tremendo'
print(list(filter(lambda x: x in 'aeiou', frase)))
print([x for x in frase if x in 'aeiou'])
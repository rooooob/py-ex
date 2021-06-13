# Extraer las consonantes mayusculas desde un texto
frase = 'PyThOn Es TrEmeNDo'
consonantes_mayusculas = list(filter(lambda x: x not in 'AEIOU' and x.isupper(), frase))
print(consonantes_mayusculas)

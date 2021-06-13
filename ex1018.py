# Obtener la longitud de cada cadena de una lista usando map

def l_cadenas(cadenas):
    if (len(cadenas) == 0):
        raise Exception('No has introducido ningun valor')
    return list(map(lambda x: len(x), cadenas))

print(l_cadenas(['123', '1234', '1']))
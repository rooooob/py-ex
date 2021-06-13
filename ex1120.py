# Validar un numero de identificacion Unico
import re

pattern = r'^(?=(?:[a-z\d]*[A-Z]){2})(?=(?:\D*\d){3})(?:(\w)(?!.*\1)){10}$'

def is_valid_uid(uid):
    return re.search(pattern, uid)

# Condiciones:
# debe contener al menos dos letras mayusculas
# 3 digitos (0-9)
# solo debe contener caracteres alfanumericos
# ningun caracter debe estar repetido
# debe tener exactamente 10 caracteres

if __name__ == '__main__':
    test = [input() for _ in range(int(input()))]

    for t in test:
        print('Valid' if is_valid_uid(t) else 'Invalid')

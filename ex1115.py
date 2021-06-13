# Validar numeros de telefono con expresiones regulares
import re

if __name__ == '__main__':
    phone_numbers = [input() for _ in range(int(input()))]

    pattern = '^[789]\d{9}$'
    validator = re.compile(pattern)

    for n in phone_numbers:
        print('YES' if validator.search(n) else 'NO')




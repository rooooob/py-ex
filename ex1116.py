# Usar una expresion regular para extraer colores hexadecimales
import re

if __name__ == '__main__':
    n = int(input())

    lines = [input() for _ in range(n)]

    css = '\n'.join(lines)
    patron = r'#([0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})'

    result = re.findall(patron, css)

    for r in result: print(r)

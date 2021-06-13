# Todas las coincidencias de una subcadena en un texto
import re

if __name__ == '__main__':
    string = input()
    p = input()

    matches = re.search(p, string)
    print(matches.start(), matches.end())
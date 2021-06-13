# Encontrar ocurrencias de dos vocales contiguas usando ReEx
import re

if __name__ == '__main__':
    s = input()

    pattern = r'[aeiouAEIOU]{2,}'

    result = re.findall(pattern, s)
    print(result)
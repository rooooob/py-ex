# 7 kyu
# https://en.wikipedia.org/wiki/Square_number => square number definition
import math
def is_square(n):
    if n > 0:
        return math.sqrt(n).is_integer()

print(is_square(-1))
print(is_square(4))
print(is_square(26))
print(is_square(25))


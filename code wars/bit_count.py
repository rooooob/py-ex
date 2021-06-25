#5 kyu
#The binary representation of 1234 is 10011010010, so the function should return 5 in this case

def count_bits(n):
    return bin(n).count('1')


print(count_bits(10))
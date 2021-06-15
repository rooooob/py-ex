# Utilizar la funcion eval() para evaluar expresiones

# ejemplo
x =  3
print('x + 3') # x + 3
print(eval('x + 3')) # 6

if __name__ == '__main__':
    expression = input()
    print(eval(expression))
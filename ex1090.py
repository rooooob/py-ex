# 1090 Evaluar un polinomio desde una variable x y una constante k

if __name__ == '__main__':
    x, k = tuple(map(int, input().split()))
    polynomial = input()
    p = polynomial.replace('x', f'{x}')

    print(eval(p) == k) # eval resuelve esta expresion
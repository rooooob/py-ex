# Demostracion de las funciones any() y all()

# any() -> retorna True si alguno de los elementos del iterable es true
# si el iterable esta vacio retornara False
print(any([1>0, 1==0, 1<0])) # True 1 > 0
print(any([1<0, 2==1, 3<2])) # False

# all() -> retorna True si todos los elementos del iterable son true. 
# si este esta vacio retornara True
print(all(['a'<'b', 'b'<'c '])) # True
print(all(['a'<'b', 'c'<'b'])) # False

# Ex
# Dada una entrada de una lista de numeros entereos separados por un espacio
# Si todos los enteros son positivos verifica si alguno es un palindromo
# resolver en menos de 3 lineas de codigo

if __name__ == '__main__':
    ls = list(map(int, input().split()))
    print(any([str(x)[::-1] == str(x) for x in ls if all([x > 0 for x in ls])]))
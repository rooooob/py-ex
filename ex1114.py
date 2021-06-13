# Usar una funcion decoradora para formatear numeros de telfono

def wrapper(f):
    def fun(l):
        l = [p[-10:] for p in l]
        l = ['+91 ' + p[:5] + ' ' + p[-5:] for p in l]
        f(l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)


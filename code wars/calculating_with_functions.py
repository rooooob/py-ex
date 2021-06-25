# 5 kyu

def zero(*args):
    pass

def one(*args):
    if not args:
        return 1
    else:
        for arg in args:
            arg()

def two(*args):
    pass

def plus(*args):
    pass

def test(func):
    
    def inner1():
        x = func()
        x + 1
        print('a')
    return inner1

def test2():
    return 2

print(one())
x = test(test2)
#print(x)
x()


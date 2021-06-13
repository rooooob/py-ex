# Crear una funcion decoradora para formatear datos de presonas
import operator 

def person_lister(f):
    
    def inner(people):
        people = sorted(people, key=lambda p: int(p[2]))

        result = []

        for p in people:
            result.append(f(p))

        return result   

    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == 'M' else 'Ms. ') + person[0] + ' ' + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
import random
TuplaEjemplo=(1,10,50,4)   #Son datos inmotables, es decir, no se puede modificar, solamente desde código
print(TuplaEjemplo[2])

TumplaRandom=tuple(random.randint(1,100) for _ in range(10))
print(TumplaRandom)

ListaTupla=[(1,2,3),(4,5,6)]

for i in ListaTupla:
    print(i)
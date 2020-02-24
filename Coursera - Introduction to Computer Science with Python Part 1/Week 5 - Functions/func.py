def soma(x,y,z):
    return x + y + z

def multiplica(x,y,z):
    return x * y * z

def fatorial (n):
    i = n - 1
    while (i > 0):
        n = n * i
        i = i - 1
    return (n)

def coeficienteBinominal(n , k):
    return fatorial(n) // (fatorial(k) * fatorial(n - k))

def delta(a,b,c):
    return (b ** 2) - (4 * ( a * c ))

import math

def raiz1(delta,a,b):
    return (-b + math.sqrt(delta)) / (2 * a)

def raiz2(delta,a,b):
    return (-b - math.sqrt(delta)) / (2 * a)

def bhaskara (a,b,c):
    if delta(a,b,c) < 0:
        print("esta equação não possui raízes reais")
    else:
        if delta(a,b,c) == 0:
            print(raiz1(delta(a,b,c),a,b))
        else:
            if (raiz1(delta(a,b,c),a,b) < raiz2(delta(a,b,c),a,b)):
                print(raiz1(delta(a,b,c),a,b), raiz2(delta(a,b,c),a,b))
            else:
                print(raiz2(delta(a,b,c),a,b), raiz1(delta(a,b,c),a,b))

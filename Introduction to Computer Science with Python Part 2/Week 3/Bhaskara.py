import math

class Bhaskara:
    def delta(num,a,b,c):
        return (b ** 2) - (4 * ( a * c ))

    def main(num):
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))
        print(num.calcula_raizes(a,b,c))

    def calcula_raizes(num,a,b,c):
        d = num.delta(a,b,c)
        if d < 0:
            return (0)
        else:
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            if d == 0:
                return (1, raiz1)
            else:
                raiz2 = (-b - math.sqrt(d)) / (2 * a)
                return (2, raiz1, raiz2)

n = int(input("Digite um numero inteiro > 1: "))

fatorPrimo = 2
multiplicidade = 0

while (n > 1):
    while (n % fatorPrimo == 0):
        multiplicidade = multiplicidade + 1
        n = n / fatorPrimo
    if multiplicidade > 0:
        print("fator ", fatorPrimo, "multiplicidade = ", multiplicidade)
    fatorPrimo = fatorPrimo + 1
    multiplicidade = 0

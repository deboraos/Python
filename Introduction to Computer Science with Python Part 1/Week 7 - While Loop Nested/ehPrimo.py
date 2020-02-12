def éPrimo(x):
    fator = 2
    while (fator * fator <= x):
        if (x % fator == 0):
            return False
        fator = fator + 1
    return True

n = 1
while (n > 0):
    n = int(input("Digite um numero inteiro positivo (0 para sair): "))
    if éPrimo(n):
        print(n, "é primo.")
    else:
        print(n, "não é primo.")

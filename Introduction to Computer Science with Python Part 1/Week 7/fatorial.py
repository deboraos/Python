n = 1

while (n > 0):
    n = int(input("Digite um numero inteiro positivo (0 para sair): "))
    i = n - 1
    while (i > 0):
        n = n * i
        i = i - 1
    print(n)

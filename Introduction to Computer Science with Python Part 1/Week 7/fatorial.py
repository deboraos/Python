n = 1

def fatorial (n):
    i = fat = 1
    while (i <= n):
        fat = fat * i
        i = i + 1
    print(fat)

while (n > 0):
    n = int(input("Digite um numero inteiro positivo (0 para sair): "))
    fatorial(n)

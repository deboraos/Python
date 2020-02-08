k = int(input("Digite um número inteiro: "))
i = 2

while (i * i <= k):
    if (k % i == 0):
        print(False)
    else:
        i = i + 1
print(i)

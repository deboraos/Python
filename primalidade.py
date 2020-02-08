n = int(input("Digite um número inteiro: "))
i = 2
primo = True

while (i < n and primo):
    primo = not ((n % i) == 0)
    i = i + 1

if (primo):
    print("primo")
else:
    print("não primo")

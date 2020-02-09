n = int(input("Digite o valor de n: "))
i = n - 1

while (i > 0):
    n = n * i
    i = i - 1

if n == 0:
    print(1)
else:
    print(n)

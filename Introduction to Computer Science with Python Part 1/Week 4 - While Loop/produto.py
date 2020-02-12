quantidade = int(input("Digite a quantidade de valores que deseja multiplicar: "))

produto = 1
i = 0

while i < quantidade:
    valor = int(input("Digite um valor a ser multiplicado: "))
    produto = produto * valor
    i = i + 1

print("O produto dos valores digitados é:", produto)

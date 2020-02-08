numero = int(input("Digite um número inteiro: "))

soma = 0
resto = 0

while numero != 0:
    soma = soma + (numero % 10)
    resto = numero // 10
    numero = resto

print(soma)

numero = int(input("Digite um numero: "))

soma = 0
resto = 0

while numero != 0:
    soma = soma + (numero % 10)
    resto = numero // 10
    numero = resto

print("A soma dos digitos é:", soma)

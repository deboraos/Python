adjacente = False
numero = int(input("Digite um numero: "))
numeroAdjacente = 0
outroNumero = 0

while numero != 0 and not adjacente:
    numeroAdjacente = numero % 10
    outroNumero = numero // 10
    if numeroAdjacente == (outroNumero % 10):
        adjacente = True
    numero = outroNumero

if adjacente:
    print("Ha dois digitos adjacentes iguais nesse numero. :)")
else:
    print("Nao ha dois digitos adjacentes iguais nesse numero. :(")

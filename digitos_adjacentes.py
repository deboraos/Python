adjacente = False
numero = int(input("Digite um número inteiro: "))
numeroAdjacente = 0
outroNumero = 0

while numero != 0 and not adjacente:
    numeroAdjacente = numero % 10
    outroNumero = numero // 10
    if numeroAdjacente == (outroNumero % 10):
        adjacente = True
    numero = outroNumero

if adjacente:
    print("sim")
else:
    print("não")

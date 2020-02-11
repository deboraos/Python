lista = []
n = 1

while (n != 0):
    n = int(input("Digite um número (0 para sair): "))
    lista.append(n)

tam = len(lista) - 1

print(len(lista))

while (tam >= 0):
    print (lista[tam], end =" ")
    tam = tam - 1

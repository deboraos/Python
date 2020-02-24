lista = []
n = 1

while (n != 0):
    n = int(input("Digite um número: "))
    if (n != 0):
        lista.append(n)
    else:
        break

tam = len(lista) - 1

while (tam >= 0):
    print (lista[tam])
    tam = tam - 1

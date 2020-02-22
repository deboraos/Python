def ordenada(lista):
    posicao = 0
    for i in range(len(lista)):
        posicao = i + 1
        if posicao < len(lista):
            if lista[i] > lista[posicao]:
                return False
    return True

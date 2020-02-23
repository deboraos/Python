def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2

    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    return merge(esquerda, direita)

def merge(esquerda, direita):
    if not esquerda:
        return direita

    if not direita:
        return esquerda

    if (esquerda[0] < direita[0]):
        return esquerda[0] + merge(esquerda[1:], direita)

    return direita[0] + merge(esquerda, direita[1:])

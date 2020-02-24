def encontra_impares(lista):
    if (len(lista) == 0):
        return []
    else:
        if (lista[0] % 2 > 0):
            l = [lista[0]]
        else:
            l = []
        impares = l + encontra_impares(lista[1:])
    return impares

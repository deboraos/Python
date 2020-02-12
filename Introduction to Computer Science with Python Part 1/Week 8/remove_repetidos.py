def remove_repetidos (lista1):
    lista2 = []
    for i in lista1:
        if i not in lista2:
            lista2.append(i)
    lista2.sort()
    return lista2

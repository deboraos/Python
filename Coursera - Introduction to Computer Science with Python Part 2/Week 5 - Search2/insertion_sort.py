def insertion_sort(lista):
    fim = len(lista)

    for i in range(fim - 1):
        ordenador = i

        for j in range(i+1, fim):
            if (lista[j] < lista[ordenador]):
                ordenador = j
        lista[i], lista[ordenador] = lista[ordenador], lista[i]
    return lista

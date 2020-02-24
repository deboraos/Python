class Ordenador:
    def selecao_direta (l, lista):
        fim = len(lista)

        for i in range(fim - 1):
            posicao_do_minimo = i
            for j in range(i+1, fim):
                if (lista[j] < lista[posicao_do_minimo]):
                    posicao_do_minimo = j
            lista [i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]

    def bolha (l, lista):
        fim = len(lista)

        for i in range(fim-1,0,-1):
            for j in range(i):
                if (lista[j] > lista[j+1]):
                    lista[j], lista[j+1] = lista[j+1], lista[j]

    def bolha_curta (l, lista):
        fim = len(lista)

        for i in range(fim-1,0,-1):
            troca = False
            for j in range(i):
                if (lista[j] > lista[j+1]):
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    troca = True
                if troca == False:
                    return

    def insercao_direta(l, lista):
        fim = len(lista)

        for i in range(fim - 1):
            ordenador = i

            for j in range(i+1, fim):
                if (lista[j] < lista[ordenador]):
                    ordenador = j
            lista[i], lista[ordenador] = lista[ordenador], lista[i]
        return lista

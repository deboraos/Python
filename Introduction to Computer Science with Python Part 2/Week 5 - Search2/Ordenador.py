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
        for i in range(1, n):
            ordenador = lista[i]
            j = i-1
            while (j > -1 and lista[j] > ordenador):
                lista[j+1] = lista[j]
                j -= 1
            lista[j+1] = ordenador   

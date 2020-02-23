import Ordenador
import random
import time
import Buscador

class ContaTempos:
    def lista_aleatoria(list, n):
        lista = [random.randrange(1000) for x in range(n)]
        return lista

    def lista_quase_ordenada(l,n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista

    def compara(l, n):
        print("Listas aleatórias")
        lista1 = l.lista_aleatoria(n)
        lista2 = lista1[:]
        lista3 = lista2[:]

        o = Ordenador.Ordenador()
        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print("Bolha demorou ", depois - antes)

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("Seleção direta demorou ", depois - antes)

        antes = time.time()
        o.bolha_curta(lista3)
        depois = time.time()
        print("Bolha curta demorou ", depois - antes)

        print("Listas quase ordenadas")
        lista1 = l.lista_quase_ordenada(n)
        lista2 = lista1[:]
        lista3 = lista2[:]

        o = Ordenador.Ordenador()
        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print("Bolha demorou ", depois - antes)

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("Seleção direta demorou ", depois - antes)

        antes = time.time()
        o.bolha_curta(lista3)
        depois = time.time()
        print("Bolha curta demorou ", depois - antes)

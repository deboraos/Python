import Ordenador
import pytest
import contaTempos

class TestaOrdenador:
    @pytest.fixture
    def o(lista):
        return Ordenador.Ordenador()

    @pytest.fixture
    def l_quase(lista):
        c = contaTempos.ContaTempos()
        return c.lista_quase_ordenada(100)

    @pytest.fixture
    def lista_aleat(lista):
        c = contaTempos.ContaTempos()
        return c.lista_aleatoria(100)

    def ordenada(l,lista):
        for i in range(len(lista)-1):
            if(lista[i] > lista[i+1]):
                return False
            return True

    def test_bolha_curta_aleat(l, o, lista_aleat):
        o.bolha_curta(lista_aleat)
        assert l.ordenada(lista_aleat)

    def test_selecao_direta_aleat(l, o, lista_aleat):
        o.selecao_direta(lista_aleat)
        assert l.ordenada(lista_aleat)

    def test_bolha_curta_quase(l, o, l_quase):
        o.bolha_curta(l_quase)
        assert l.ordenada(l_quase)

    def test_selecao_direta_quase(l, o, l_quase):
        o.selecao_direta(l_quase)
        assert l.ordenada(l_quase)

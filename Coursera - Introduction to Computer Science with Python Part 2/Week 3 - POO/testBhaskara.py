import Bhaskara

class TestBhaskara:

    @pytest.fixture
    def b(num):
        return Bhaskara.Bhaskara()

    def testa_uma_raiz(num):
        assert b.calcula_raizes(1, 0, 0) == (1, 0)

    def testa_duas_raizes(num):
        b = Bhaskara.Bhaskara()
        assert b.calcula_raizes(1, -5, 6) == (2, 3, 2)

    def testa_nenhuma_raiz(num):
        b = Bhaskara.Bhaskara()
        assert b.calcula_raizes(10, 10, 10) == (0)

    def testa_raiz_negativa(num):
        b = Bhaskara.Bhaskara()
        assert b.calcula_raizes(10, 20, 10) == (1, -1)

def quadrado(num):
    return num ** 2

def cubo(num):
    return num ** 3

funcoes = [quadrado, cubo]
lista = [0, 1, 2, 3, 4]

for i in lista:
    resultado = map(lambda num: num(i), funcoes)
    print(list(resultado))

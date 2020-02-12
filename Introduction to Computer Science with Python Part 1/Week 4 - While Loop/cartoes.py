cartao = int(input("Digite o numero do seu cartao: "))

cartaoEncontrado = False
cartaoLido = 1

while cartaoLido != 0 and not cartaoEncontrado:
    cartaoLido = int(input("Digite o numero do proximo cartao: "))
    if cartaoLido == cartao:
        cartaoEncontrado = True

if cartaoEncontrado:
    print("Cartao encontrado!")
else:
    print("Cartao nao encontrado.")

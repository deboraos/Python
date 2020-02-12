l = int(input("digite a largura: "))
a = int(input("digite a altura: "))

linha = 1
coluna = 1

while (linha <= a):
    while (coluna <= l):
        print("#", end = "")
        coluna = coluna + 1
    print("")
    linha = linha + 1
    coluna = 1

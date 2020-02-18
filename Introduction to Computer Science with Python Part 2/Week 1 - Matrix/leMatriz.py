def imprimeMatriz(m):
    l = len(m)
    c = len(m[0])
    for i in range(l):
        for j in range(c):
            if(j == c - 1):
                print("%d" %m[i][j])
            else:
                print("%d" %m[i][j], end = " ")
        
def criaMatriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            valor = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]"))
            linha.append(valor)
        matriz.append(linha)
    return imprimeMatriz(matriz)

def leMatriz():
    lin = int(input("Digite o numero de linhas da matriz: "))
    col = int(input("Digite o numero de colunas da matriz: "))
    return criaMatriz(lin, col)

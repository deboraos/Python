def imprime_matriz(matriz):
    l = len(matriz)
    c = len(matriz[0])
    for i in range(l):
        for j in range(c):
            if(j == c - 1):
                print(matriz[i][j], end = "")
            else:
                print(matriz[i][j], end = " ")
        print()

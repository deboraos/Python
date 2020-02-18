def imprime_matriz(matriz):
    l = len(matriz)
    c = len(matriz[0])
    for i in range(l):
        for j in range(c):
            if(j == c - 1):
                print("%d" %matriz[i][j])
            else:
                print("%d" %matriz[i][j], end = " ")

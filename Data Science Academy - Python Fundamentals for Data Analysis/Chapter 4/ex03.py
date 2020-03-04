def transposta(matriz):
    aux=[]
    for j in range(len(matriz[0])):
        l=[]
        for i in range(len(matriz)):
            l.append(matriz[i][j])
        aux.append(l)
    return aux

matrix = [[1, 2],[3,4],[5,6],[7,8]]

print(transposta(matrix))

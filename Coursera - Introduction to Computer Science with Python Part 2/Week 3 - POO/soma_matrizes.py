import Matriz

def soma_matrizes (A, B):
    lin = len(A)
    col = len(A[0])
    C = Matriz.criaMatriz(lin, col, 0)

    for i in range(lin):
        for j in range(col):
            C[i][j] = A[i][j] + B[i][j]
    return C

if __name__ == '__main__':
    A = [[1,2,3],[4,5,6],[7,8,9]]
    B = [[10,20,30],[40,50,60],[70,80,90]]
    print(soma_matrizes(A,B))

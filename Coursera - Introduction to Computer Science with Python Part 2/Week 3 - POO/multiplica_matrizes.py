import Matriz

def multiplica_matrizes (A, B):
    linA, colA = len(A), len(A[0])
    linB, colB = len(B), len(B[0])
    assert colA == linB
    C = []

    for i in range(linA):
        C.append([])
        for j in range(colB):
            C[i].append(0)
            for k in range(colA):
                C[i][j] += A[i][k] * B[k][j]
    return C

if __name__ == '__main__':
    A = [[1,2,3],[4,5,6]]
    B = [[1,2],[3,4],[5,6]]
    print(multiplica_matrizes(A,B))

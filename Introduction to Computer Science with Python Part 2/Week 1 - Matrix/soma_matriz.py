def soma_matrizes(m1, m2):
    linm1 = len(m1)
    linm2 = len(m2)
    colm1 = len(m1[0])
    colm2 = len(m2[0])
    if (linm1 == linm2) and (colm1 == colm2):
        m3 = []
        for i in range(linm1):
            m3.append([])
            for j in range(colm1):
                soma = (m1[i][j] + m2[i][j])
                m3[i].append(soma)
        return m3
    else:
        return False

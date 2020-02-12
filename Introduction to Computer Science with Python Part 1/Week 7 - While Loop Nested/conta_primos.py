def éPrimo(x):
    fator = 2
    while (fator * fator <= x):
        if (x % fator == 0):
            return False
        fator = fator + 1
    return True

def n_primos(k):
    qtd = 0
    i = 2
    while i <= k:
        if éPrimo(i):
            qtd = qtd + 1
        i = i + 1
    return qtd

def éPrimo(k):
    i = 2
    while (i * i <= k):
        if (k % i == 0):
            return False
        i = i + 1
    return True

def maior_primo(n):
    p = n
    while (p > 2):
        if éPrimo(p):
            return p
        p = p - 1
    return 2

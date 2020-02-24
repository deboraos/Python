def hipotenusa(a, b):
    return ((a ** 2) + (b ** 2))

def soma_hipotenusas (n):
    c = 1
    soma = 0
    while (c <= n):
        h = c ** 2
        a = 1
        b = 1
        while (a < n):
            while (b < n):
                if (h == hipotenusa(a, b)):
                    soma = soma + c
                    a = n
                    break
                b = b + 1
            a = a + 1
            b = a
        c = c + 1
    return soma

def conta_letras(frase, contar="vogais"):
    total = 0
    if (contar == "vogais"):
        for i in range(len(frase)):
            if (frase[i] in ['a', 'e', 'i', 'o', 'u']):
                total += 1
    if (contar == "consoantes"):
        for i in range(len(frase)):
            if (frase[i] in ['b','c','d','f','g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']):
                total += 1
    return total

print(conta_letras('programamos em python'))
print(conta_letras('programamos em python', 'vogais'))
print(conta_letras('programamos em python', 'consoantes'))

def primeiro_lex(lista):
    primeiro_lex = lista[0]
    for i in lista:
        if (i < primeiro_lex):
            primeiro_lex = i
    return primeiro_lex

print(primeiro_lex(["maria", "José", "ana", "aadia", "Valdemar"]))
print(primeiro_lex(['oĺá', 'A', 'a', 'casa']))
print(primeiro_lex(['AAAAAA', 'b']))

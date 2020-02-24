def menor_string(lista):
    menor_string = lista[0].lower()
    for i in lista:
        if (i.lower() < menor_string):
            menor_string = i.lower()
    return menor_string

def teste_menor_string():
    return menor_string(["maria", "José", "ana", "aadia", "Valdemar"])

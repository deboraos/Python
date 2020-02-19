def mais_curto(lista):
    mais_curto = lista[0].strip()
    for i in lista:
        if (len(i.strip()) < len(mais_curto)):
            mais_curto = i.strip()
    return mais_curto

def teste_mais_curto():
    return mais_curto(["Arquibaldo", "          ana     ", "josé", "    Alouhis   "])

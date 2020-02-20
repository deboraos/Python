def menor_nome(nomes):
    menor_nome = nomes[0].strip()
    for i in nomes:
        if (len(i.strip()) < len(menor_nome)):
            menor_nome = i.strip()
    return menor_nome.capitalize()

print(menor_nome(["Arquibaldo", "          ana     ", "josé", "    Alouhis   "]))
print(menor_nome(['maria', 'josé', 'PAULO', 'Catarina']))
print(menor_nome(['maria', ' josé  ', '  PAULO', 'Catarina  ']))
print(menor_nome(['Bárbara', 'JOSÉ  ', 'Bill']))

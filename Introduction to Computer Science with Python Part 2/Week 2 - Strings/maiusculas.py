def maiusculas(frase):
    maiusculas = ""
    for i in range(len(frase)):
        if(ord(frase[i]) >= 65 and ord(frase[i]) <= 90):
            maiusculas += frase[i]
    return maiusculas

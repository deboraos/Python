def maiusculas(frase):
    maiusculas = ""
    for i in range(len(frase)):
        if(ord(frase[i]) >= 65 and ord(frase[i]) <= 90):
            maiusculas += frase[i]
    return maiusculas

print(maiusculas('Programamos em python 2?'))
print(maiusculas('Programamos em Python 3.'))
print(maiusculas('PrOgRaMaMoS em python!'))

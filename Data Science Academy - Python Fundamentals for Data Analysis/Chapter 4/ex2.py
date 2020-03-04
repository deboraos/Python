def funcaoex2 (frase):
    frase.split()
    return [frase.upper(), frase.lower(), len(frase)]

frase = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()

resultado = map(funcaoex2,frase)

for i in resultado:
    print (i)

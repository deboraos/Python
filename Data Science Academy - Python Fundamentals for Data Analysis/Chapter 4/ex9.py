def chaveValor(d1,d2):
    d3 = {}
    for chaved1, valord2 in zip(dict1, dict2.values()):
        d3[chaved1] = valord2
    return d3

dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}

dict3 = chaveValor(dict1, dict2)

print(dict3)

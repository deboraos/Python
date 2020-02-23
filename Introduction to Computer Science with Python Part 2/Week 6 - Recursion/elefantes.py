def incomodam(n):
    if (n > 0):
        return "incomodam " + incomodam(n-1)
    elif (n == 1):
        return "incomodam "
    else:
        return ""

def elefantes(n):
    if (n > 2):
        return elefantes(n-1) + f"\n{n-1} elefantes incomodam muita gente" + f"\n{n} elefantes "+ incomodam(n) + "muito mais"
    elif (n == 2):
        return elefantes(n-1) + f"\n{n} elefantes "+ incomodam(n) + "muito mais"
    elif (n == 1):
        return "Um elefante incomoda muita gente"
    else:
        return ""

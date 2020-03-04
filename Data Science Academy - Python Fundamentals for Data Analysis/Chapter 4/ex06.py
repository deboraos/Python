def negativo(num):
    if (num < 0):
        return True

print(list(filter(negativo, range(-5, 5))))

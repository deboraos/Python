def minMax(temperaturas):

    print ("A menor temperatura do mes foi: ", minima(temperaturas), "C.")
    print ("A maior temperatura do mes foi: ", maxima(temperaturas), "C.")

def minima(temps):
    temps.sort()
    return temps[0]

def maxima(temps):
    temps.sort()
    return temps[-1]

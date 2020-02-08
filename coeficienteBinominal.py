def coeficienteBinominal(n , k):
    return fatorial(n) // (fatorial(k) * fatorial(n - k))

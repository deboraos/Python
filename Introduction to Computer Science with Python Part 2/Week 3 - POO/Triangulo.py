class Triangulo:
    def __init__(triangulo, a, b, c):
        triangulo.a = a
        triangulo.b = b
        triangulo.c = c

    def perimetro(triangulo):
        return triangulo.a + triangulo.b + triangulo.c

    def tipo_lado(triangulo):
        if (triangulo.a == triangulo.b and triangulo.b != triangulo.c) or (triangulo.c == triangulo.b and triangulo.b != triangulo.a) or (triangulo.c == triangulo.a and triangulo.a != triangulo.b):
            return "isósceles"
        elif (triangulo.a == triangulo.b == triangulo.c):
            return "equilátero"
        elif (triangulo.a != triangulo.b != triangulo.c):
            return "escaleno"

    def retangulo(triangulo):
        if (triangulo.c ** 2 == triangulo.a ** 2 + triangulo.b ** 2):
            return True
        else:
            return False

    def semelhantes(triangulo, t):
        if t.a / triangulo.a == t.b / triangulo.b and t.c / triangulo.c:
            return True
        else:
            return False

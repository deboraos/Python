def main():
    carro1 = Carro('brasilia', 1968, 'amarela', 80)
    carro2 = Carro('fusca', 1981, 'preto', 95)

    carro1.acelere(40)
    carro2.acelere(50)
    carro1.acelere(80)
    carro1.pare()
    carro2.acelere(100)

class Carro:
    def __init__(car, model, year, color, maxSpeed):
        car.modelo        = model
        car.ano           = year
        car.cor           = color
        car.velocidade    = 0
        car.velocidadeMax = maxSpeed

    def imprima(car):
        if car.velocidade == 0:
            print("%s %s %d"%(car.modelo, car.cor, car.ano))
        elif car.velocidade < car.velocidadeMax:
            print("%s %s indo a %dKm/h"%(car.modelo, car.cor, car.velocidade))
        else:
            print("%s %s indo muito rápido!"%(car.modelo, car.cor))

    def acelere(car, speed):
        car.velocidade = speed
        if car.velocidade > car.velocidadeMax:
            car.velocidade = car.velocidadeMax
        car.imprima()

    def pare(car):
        car.velocidade = 0
        car.imprima()

main()

class Smartphone():
    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface

class MP3Player(Smartphone):
    def __init__(self, capacidade, tamanho="Slim", interface="LCD"):
        self.capacidade = capacidade
        Smartphone.__init__(self, tamanho, interface)

Orientação a Objetos

## Exercício 1:
Crie um objeto a partir da classe abaixo, chamado roc1, passando 2 parâmetros e depois faça uma chamada aos atributos e métodos.
```python
from math import sqrt

class Rocket():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment

    def print_rocket(self):
        print(self.x, self.y)
```

## Exercício 2:
Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2 métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos especiais.

## Exercício 3:
Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.

## Link Relacionados
- [Python Orientado a Objetos](http://www.dcc.ufrj.br/~fabiom/mab225/pythonoo.pdf)
- [Python e Programação Orientada a Objetos](https://wiki.python.org.br/ProgramacaoOrientadaObjetoPython)
- [Classes e Objetos –Fundamentos](https://panda.ime.usp.br/pensepy/static/pensepy/13-Classes/classesintro.html)
- [Características da orientação a objetos](https://aprendendo-computacao-com-python.readthedocs.io/en/latest/capitulo_14.html)
- [Jogo da Forca](https://pt.wikipedia.org/wiki/Jogo_da_forca)
- [Formação Cientista de Dados](https://www.datascienceacademy.com.br/pages/formacao-cientista-de-dadosScratchhttps://scratch.mit.edu/)
- [Código e Robótica para Crianças](https://www.youtube.com/watch?v=pOMEwgHCJLk)

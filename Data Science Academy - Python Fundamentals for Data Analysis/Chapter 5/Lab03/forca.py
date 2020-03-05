# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.word = word
        self.hits = []
        self.misses = []

    # Método para adivinhar a letra
    def guess(self, letter):
        if ((letter in self.word) and (letter not in self.hits)):
            self.hits.append(letter)
        elif ((letter not in self.word) and (letter not in self.misses)):
            self.misses.append(letter)
        else:
            return False
        return True

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        if ((self.hangman_won() == True) or ((len(self.misses) == 6))):
            return  True
        else:
            return False

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if ('_' not in self.hide_word()):
            return True
        return False

    # Método para não mostrar a letra no board
    def hide_word(self):
        aux = ''
        for letter in self.word:
            if (letter not in self.hits):
                aux += '_'
            else:
                aux += letter
        return aux

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[len(self.misses)])
        print("\nPalavra: " + self.hide_word())
        print("\nErros: ", )
        for letter in self.misses:
            print(letter, )
        print("Acertos: ", )
        for letter in self.hits:
            print(letter, )

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        game.print_game_status()
        letter = input("\nLetra: ")
        game.guess(letter.lower())

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print("\nParabéns! Você venceu!!")
    else:
        print("\nGame over! Você perdeu.")
        print("A palavra era " + game.word + ".")

# Executa o programa
if __name__ == "__main__":
    main()

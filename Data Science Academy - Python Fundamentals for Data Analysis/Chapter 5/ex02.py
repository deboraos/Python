class Pessoa():
    def __init__(self, nome, cidade, telefone , email):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return "A pessoa se chama " + self.nome + ", reside na cidade de " + self.cidade + ", seus contatos são " + self.telefone + " e " + self.email

p1 = Pessoa("João da Silva","Salvador","999","joao@jao.com")
print(str(p1))

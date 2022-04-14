class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'Nome: {self.nome} - Idade: {self.idade}'

    def is_adulto(self):
        return True if self.idade > 18 else False

class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome
    
    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

if __name__ == '__main__':
    jose = Humano('José')
    grug = Humano('Grug').das_cavernas()

    print(f'Humano.especie = {Humano.especie}')
    print(f'Jose.especie = {jose.especie}')
    print(f'Grug.especie = {grug.especie}')
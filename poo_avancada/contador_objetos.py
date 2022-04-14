class ClasseSimples:
    contador = 0

    def __init__(self):
        self.adicionarUm()

    @classmethod
    def adicionarUm(cls):
        cls.contador += 1


if __name__ == '__main__':
    lista = [ClasseSimples(), ClasseSimples()]
    print(ClasseSimples.contador)

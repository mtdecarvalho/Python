class Potencia:
    def __init__(self, expoente):
        # construtor
        # self representa a instância atual
        self.expoente = expoente

    def __call__(self, base):
        # essa função será chamada quando o objeto for usado como uma função
        return base ** self.expoente


if __name__ == '__main__':
    quadrado = Potencia(2)
    cubo = Potencia(3)

    if callable(quadrado) and callable(cubo):
        print(f'3^2 => {quadrado(3)}')
        print(f'5^3 => {cubo(5)}')
        print(Potencia(4)(2))
        # como o objeto já foi criado (Potencia(4)), a função callable é chamada e retorna o valor.
        # isso é o mesmo que:
        elevarQuartaPotencia = Potencia(4)
        print(elevarQuartaPotencia(2))

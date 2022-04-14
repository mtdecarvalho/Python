class Carro:
    def __init__(self, velocidade_maxima):
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    def acelerar(self, delta=5):
        maxima = self.velocidade_maxima
        nova = self.velocidade_atual + delta

        # soluçao com operador ternario
        # self.velocidade_atual = nova if nova <= maxima else maxima
        
        # minha solucao
        if nova > maxima:
            nova = maxima
        self.velocidade_atual = nova

        return self.velocidade_atual    

    def frear(self, delta=5):
        minima = 0
        nova = self.velocidade_atual - delta

        # solucao com operador ternario
        # self.velocidade_atual = nova if nova >= 0 else 0

        # minha solucao
        if nova < minima:
            nova = minima
        self.velocidade_atual = nova

        return self.velocidade_atual

if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        print(c1.acelerar(8))
    
    for _ in range(10):
        print(c1.frear(delta=20))

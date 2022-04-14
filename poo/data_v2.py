class Data:
    def __init__(self, dia=1, mes=1, ano=1970):
        # construtor em python.
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(13, 4, 2022)
# d1.dia = 11
# d1.mes = 4
# d1.ano = 2022
print(d1)

d2 = Data(ano=2022)
d2.dia = 7
# d2.mes = 11
# d2.ano = 2020
print(d2)

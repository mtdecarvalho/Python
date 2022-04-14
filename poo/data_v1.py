class Data:
    def to_str(self):
        # pode colocar qualquer nome que queira no lugar de self, porém self é o padrão.
        return f'{self.dia}/{self.mes}/{self.ano}'
    def __str__(self):
        # esse é um metodo suportado por todos os objetos do python que será usado sempre 
        # que o python precisar converter um objeto para string. isso torna o método acima obsoleto e pode ser
        # usado para substitui-lo, sendo necessario apenas usar print(objeto) ao inves de print(objeto.to_str())
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data() # declarando um objeto
# python permite a criação de objeto com atributos não definidos na classe
d1.dia = 11
d1.mes = 4
d1.ano = 2022
print(d1)

d2 = Data()
d2.dia = 7
d2.mes = 11
d2.ano = 2020
print(d2)

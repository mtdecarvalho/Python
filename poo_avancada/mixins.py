class HtmlToStringMixin:
    def __str__(self):
        # Conversão para HTML
        html = super().__str__() \
            .replace('(', '<strong>(') \
            .replace(')', ')</strong>')
        return f'<span>{html}</span>'

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def __str__(self):
        return self.nome


class Animal:
    def __init__(self, nome, pet=True):
        self.nome = nome
        self.pet = pet
    
    def __str__(self):
        return self.nome + ' (pet)' if self.pet else ''
    

class PessoaHtml(HtmlToStringMixin, Pessoa):
    # no caso de herança multipla, a ordem é importante.
    # neste caso htmltostringmixin prevalecerá sobre pessoa, então quando
    # esta classe for impressa como string, será usado o __str__ de HtmlToStringMixin que fará a mistura de seu conteúdo com o __str__ de Pessoa.
    # caso a ordem fosse invertida, seria chamada apenas o __str__ de Pessoa, já que 
    # a função não fará nenhum tipo de mistura e retornará apenas a variavel
    pass


class AnimalHtml(HtmlToStringMixin, Animal):
    pass


if __name__ == '__main__':
    p1 = Pessoa('juliana')
    print(p1)

    p2 = PessoaHtml('Kazuma Kiryu')
    print(p2)

    toto = AnimalHtml('Totó')
    print(toto)
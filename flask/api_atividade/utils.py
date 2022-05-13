from models import Pessoas


def inserir_pessoas():
    pessoa = Pessoas(nome='Juliana',idade=19)
    print(pessoa)
    pessoa.save()


def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    # pessoa = Pessoas.query.filter_by(nome='Theus').first()
    # print(pessoa.idade)


def alterar_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Juliana').first()
    pessoa.nome = 'Jusinha'
    pessoa.save()


def excluir_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Tetheuso').first()
    pessoa.delete()


if __name__ == '__main__':
    # inserir_pessoas()
    # alterar_pessoa()
    consulta_pessoas()
    excluir_pessoa()
    consulta_pessoas()



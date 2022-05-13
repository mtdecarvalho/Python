from models import Pessoas, Usuarios


def inserir_pessoas():
    pessoa = Pessoas(nome='Juliana', idade=19)
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


def inserir_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    # inserir_usuario('matheus', '123')
    # inserir_usuario('juliana', '321')
    consulta_todos_usuarios()

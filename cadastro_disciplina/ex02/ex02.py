import os

class Disciplina:
    def __init__(self, codigo, nome, professor, creditos, ano, semestre, nota1, nota2, media):
        self.codigo = codigo
        self.nome = nome
        self.professor = professor
        self.creditos = creditos
        self.ano = ano
        self.semestre = semestre
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = (self.nota1 + 2.0*self.nota2)/3.0

    def __str__(self):
        return  "Codigo    : {0:0>4}\n"\
                "Nome      : {1}\n"\
                "Professor : {2}\n"\
                "Creditos  : {3}\n"\
                "Ano       : {4}\n"\
                "Semestre  : {5}\n"\
                "Nota1     : {6:.2f}\n"\
                "Nota2     : {7:.2f}\n"\
                "Media     : {8:.2f}\n".format(
                    self.codigo, self.nome, self.professor,
                    self.creditos, self.ano, self.semestre,
                    self.nota1, self.nota2, self.media
                )


def criar_disciplina():
    print('Codigo: ', end = '')
    codigo = int(input())
    print('Nome: ', end = '')
    nome = input()
    print('Professor: ', end = '')
    professor = input()
    print('Creditos: ', end = '')
    creditos = int(input())
    print('Ano: ', end = '')
    ano = int(input())
    print('Semestre: ', end = '')
    semestre = int(input())
    print('Nota 1: ', end = '')
    nota1 = float(input())
    print('Nota 2: ', end = '')
    nota2 = float(input(), end = '')
    media = (nota1 + 2.0*nota2)/3.0
    return Disciplina(codigo, nome, professor, creditos, ano, semestre, nota1, nota2, media)

def mostrar_disciplina():
    ok = ''
    while ok != 'Ok':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(disciplina)
        ok = input()


if __name__ == '__main__':

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Bem vindo ao cadastro de disciplinas!")
        print("1 - Ler dados da disciplina")
        print("2 - Mostrar os dados da disciplina")
        opcao = int(input())

        if opcao == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            disciplina = criar_disciplina()
        elif opcao == 2:
            mostrar_disciplina()
        elif opcao == 3:
            exit()



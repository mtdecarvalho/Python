from dis import dis
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
        return  "{0:0>4} {1:<50} {2:>4} {3:>4}/{4:>1} {5:.2f}\n".format(
                    self.codigo, self.nome, self.creditos,
                    self.ano, self.semestre, self.media
                )


class Historico:
    def __init__(self):
        self.lista_disciplinas = []
    
    def adicionar_disciplina(self, Disciplina):
        self.lista_disciplinas.append(Disciplina)
    
    def listar_historico(self):
        ok = ''
        while ok != 'Ok':
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Cod. Nome                                               Cred  Ano/S Media')
            for disciplina in self.lista_disciplinas:
                print(disciplina)
            ok = input()

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
    nota2 = float(input())
    media = (nota1 + 2.0*nota2)/3.0
    return Disciplina(codigo, nome, professor, creditos, ano, semestre, nota1, nota2, media)
    
if __name__ == '__main__':

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Bem vindo ao cadastro de disciplinas!")
        print("1 - Inicializar histórico")
        print("2 - Inserir uma nova disciplina")
        print("3 - Listar histórico")
        print("4 - Sair")
        opcao = int(input())

        if opcao == 1:
            historico = Historico()
        elif opcao == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            historico.adicionar_disciplina(criar_disciplina())
        elif opcao == 3:
            historico.listar_historico()
        elif opcao == 4:
            print("Obrigado por utilizar o programa de cadastro, volte sempre!")
            exit()


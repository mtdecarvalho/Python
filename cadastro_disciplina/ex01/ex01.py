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
    codigo = int(input())
    nome = input()
    professor = input()
    creditos = int(input())
    ano = int(input())
    semestre = int(input())
    nota1 = float(input())
    nota2 = float(input())
    media = (nota1 + 2.0*nota2)/3.0
    return Disciplina(codigo, nome, professor, creditos, ano, semestre, nota1, nota2, media)

if __name__ == "__main__":
    disciplina = criar_disciplina()
    print(disciplina)
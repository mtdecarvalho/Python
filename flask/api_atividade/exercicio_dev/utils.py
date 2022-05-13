from exercicio_dev.models import Programador, Habilidades, Programador_Habilidade


def consultar_tudo():
    programador = Programador.query.all()
    print(programador)
    habilidades = Habilidades.query.all()
    print(habilidades)
    programador_habilidade = Programador_Habilidade.query_all()
    print(programador_habilidade)
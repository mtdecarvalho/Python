from datetime import date, datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()
        # a introduçao deste metodo na classe permite que ela seja iteravel.
        # note abaixo nos laços for

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        # possivel IndexError
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('(Concluído)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dias)')

        return f'{self.descricao} ' + ' '.join(status)


class TarefaRecorrente(Tarefa):
    # essa é uma subclasse que vai herdar da superclasse tarefa.
    def __init__(self, descricao, vencimento=None, dias=7):
        super().__init__(descricao, vencimento)
        # desta forma é chamado o construtor da superclasse (tarefa)
        self.dias = dias

    def concluir(self):
        super().concluir()
        # desta forma é chamada a função concluir da superclasse Tarefa
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        return TarefaRecorrente(self.descricao, novo_vencimento, self.dias)


def main():
    casa = Projeto('Tarefas de casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Lavar prato')
    casa.tarefas.append(TarefaRecorrente('Trocar lencois', datetime.now(), 7))
    casa.tarefas.append(casa.procurar('Trocar lencois').concluir())
    print(casa)

    casa.procurar('Lavar prato').concluir()
    for tarefa in casa:  # como Projeto agora é iterável, nao se torna mais necessário usar casa.tarefas
        print(f' - {tarefa}')

    print(casa)

    mercado = Projeto('Compras do mercado')
    mercado.add('Farofa')
    mercado.add('Sucrilhos')
    mercado.add('Desodorante')
    mercado.add('Arroz', datetime.now() + timedelta(days=3, minutes=12))
    print(mercado)

    comprar_farofa = mercado.procurar('Farofa')
    comprar_farofa.concluir()
    for tarefa in mercado:  # como Projeto agora é iterável, nao se torna mais necessario usar mercado.tarefas
        print(f' - {tarefa}')
    print(mercado)


if __name__ == '__main__':
    main()

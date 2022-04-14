from datetime import date, datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    # sobrecarga de operador do operador +=
    # projeto += tarefa
    # desta forma, tarefa define o dono (tarefa.dono) como projeto (self)
    # e logo em seguida é adicionada uma nova tarefa dentro do projeto (self)
    # e finalmente ocorre o retorno do projeto (self).
    def __iadd__(self, tarefa):
        tarefa.dono = self
        self._add_tarefa(tarefa)
        return self

    def _add_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    def add(self, tarefa, vencimento=None, **kwargs):
        funcao_escolhida = self._add_tarefa if isinstance(
            tarefa, Tarefa) else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)

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
    def __init__(self, descricao, vencimento=None, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias
        self.dono = None

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        nova_tarefa = TarefaRecorrente(
            self.descricao, novo_vencimento, self.dias)
        if self.dono:
            # aqui é checado se esta tarefa já possui dono
            self.dono += nova_tarefa
            # caso tenha, essa tarefa será adicionada para dentro do dono
        return nova_tarefa


def main():
    casa = Projeto('Tarefas de casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Lavar prato')
    casa += TarefaRecorrente('Trocar lencois', datetime.now(), 7)
    # desta forma será criada uma nova tarefarecorrente que será adicionada para dentro de casa
    casa.procurar('Trocar lencois').concluir()
    # como a tarefa já tem dono definido, ela criará uma nova tarefa também dentro de casa
    print(casa)

    casa.procurar('Lavar prato').concluir()
    for tarefa in casa:
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
    for tarefa in mercado:
        print(f' - {tarefa}')
    print(mercado)


if __name__ == '__main__':
    main()

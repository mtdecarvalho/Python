from datetime import date, datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def _add_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    # as duas funcoes acima possuem os mesmos argumentos para que possam ser chamadas de forma igual.

    def add(self, tarefa, vencimento=None, **kwargs):
        # essa funcao vai funcionar de duas formas:
        funcao_escolhida = self._add_tarefa if isinstance(
            tarefa, Tarefa) else self._add_nova_tarefa
        # primeiro ela checa se a tarefa passada é da classe Tarefa (TarefaRecorrente também é Tarefa)
        # caso seja, a função _add_tarefa é chamada. caso contrário, tarefa não é uma Tarefa e sim uma
        # descrição, então é chamada a função _add_nova_funcao para que seja criada uma nova Tarefa
        # usando a descrição passada.
        # de qualquer forma, ou uma ou outra função será alocada para essa variavel
        kwargs['vencimento'] = vencimento
        # para que funcao_escolhida funcione para ambas as funcoes, o dado de vencimento é passado para
        # dentro de kwargs.
        funcao_escolhida(tarefa, **kwargs)
        # e finalmente funcao_escolhida é chamada, chamando a função apropriada pro tipo de dado passado.
        # todos os outros dados necessarios para as funcoes estao dentro de kwargs.

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

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        return TarefaRecorrente(self.descricao, novo_vencimento, self.dias)


def main():
    casa = Projeto('Tarefas de casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Lavar prato')
    casa.add(TarefaRecorrente('Trocar lencois', datetime.now(), 7))
    # é passada uma nova tarefa recorrente
    casa.add(casa.procurar('Trocar lencois').concluir())
    # cria-se uma nova tarefa com recorrencia para daqui a n dias
    # por causa de como a função add funciona agora, não se é mais necessário utilizar casa.tarefas.append
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

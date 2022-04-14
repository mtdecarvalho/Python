from .vendedor import Vendedor
from .cliente import Cliente
from .compra import Compra



__all__ = ['Cliente', 'Vendedor', 'Compra']

class Loja:
    def __init__(self, vendedores=[], clientes=[]):
        self.vendedores = vendedores
        self.clientes = clientes

    def _add_vendedor(self, vendedor, **kwargs):
        self.vendedores.append(vendedor)

    def _add_novo_vendedor(self, nome, **kwargs):
        self.vendedores.append(
            Vendedor(nome, kwargs.get('idade'), kwargs.get('salario')))

    def add_vendedor(self, nome, idade=None, salario=None, **kwargs):
        funcao_escolhida = self._add_vendedor if isinstance(
            nome, Vendedor) else self._add_novo_vendedor

        kwargs['idade'] = idade
        kwargs['salario'] = salario

        funcao_escolhida(nome, **kwargs)

    def procurar_vendedor(self, nome):
        try:
            return [vendedor for vendedor in self.vendedores if vendedor.nome == nome][0]
        except IndexError as e:
            print('Vendedor não encontrado')

    def _add_cliente(self, cliente, **kwargs):
        self.clientes.append(cliente)

    def _add_novo_cliente(self, nome, **kwargs):
        self.clientes.append(Cliente(nome, kwargs.get('idade')))

    def add_cliente(self, nome, idade=None, **kwargs):
        funcao_escolhida = self._add_cliente if isinstance(
            nome, Cliente) else self._add_novo_cliente

        kwargs['idade'] = idade

        funcao_escolhida(nome, **kwargs)

    def procurar_cliente(self, nome):
        try:
            return [cliente for cliente in self.clientes if cliente.nome == nome][0]
        except IndexError as e:
            print("Cliente não encontrado")

    def add_compra(self, nome_cliente, nome_vendedor, data, valor):
        self.procurar_cliente(nome_cliente).registrar_compra(
            Compra(nome_vendedor, data, valor))

    def get_data_ultima_compra(self, nome):
        return self.procurar_cliente(nome).get_data_ultima_compra()

    def get_total_compras(self, nome):
        return self.procurar_cliente(nome).total_compras()

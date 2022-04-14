from datetime import datetime
from loja import Loja, Cliente, Vendedor

if __name__ == '__main__':
    steam = Loja()
    theus = Vendedor('theus', 21, 10000)
    steam.add_vendedor(theus)
    print(steam.procurar_vendedor('theus'))

    steam.add_vendedor('el tetheuso', idade=24, salario=1000)
    print(steam.procurar_vendedor('el tetheuso'))

    jusinha = Cliente('jusinha', 19)
    steam.add_cliente(jusinha)
    print(steam.procurar_cliente('jusinha'))
    print(steam.procurar_cliente('jusinha').is_adulto())

    steam.add_cliente('minha jusinha', idade=19, salario=1000000)
    print(steam.procurar_cliente('minha jusinha'))

    steam.procurar_cliente('nao existe')
    steam.procurar_vendedor('nao existe')

    steam.add_compra(nome_cliente='jusinha', nome_vendedor='theus',
                     data=datetime.now(), valor=3000)
    steam.add_compra(nome_cliente='jusinha', nome_vendedor='el tetheuso',
                     data=datetime.now(), valor=7000)

    print(steam.get_data_ultima_compra('jusinha'))
    print(steam.get_total_compras('jusinha'))

with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida) # print sendo direcionado para um
                                                                     # arquivo, no caso, o arquivo pessoas.txt definido acima


if arquivo.closed:
    print("ARQ FECHADO")


if saida.closed:
    print('saida fechado')

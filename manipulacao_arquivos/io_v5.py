with open('pessoas.csv') as arquivo:        # with garante que o arquivo será fechado automaticamente pelo python
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print("ARQ FECHADO")
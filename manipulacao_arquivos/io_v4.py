try:
    arquivo = open('pessoas.csv')

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
except IndexError:  # tratar erro de indice
    pass            # bloco vazio
finally:
    print("finally")
    arquivo.close()

if arquivo.closed:
    print("ARQ FECHADO")
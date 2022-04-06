arquivo = open('pessoas.csv')
for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(','))) # strip remove caracteres (por padrão whitespaces) do final e do começa de uma string
arquivo.close()

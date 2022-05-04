from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Juliana', '98765-4321'),
    ('Jusinha', '98745-4321'),
    ('Ju', '98265-4321'),
    ('Meu amor', '91765-4321'),
    ('Minha linda', '99765-4321'),
    ('Minha mulher', '94765-4321'),
    ('Matheus', '98665-4321')
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('Foram incluidos {cursor.rowcount} registros!')

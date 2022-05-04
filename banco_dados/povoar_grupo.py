from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

grupos = (
    ('Casa',),
    ('Amigos',),
    ('Minha mulher',)
)

grupos_SQL = 'INSERT INTO grupos (descricao) VALUES (%s)'

# contatos = (
#     ('Juliana', '54545-54545', 3),
#     ('JP', '12245-6789', 2),
#     ('Vini', '11345-6789', 2),
#     ('LC', '12335-6789', 2),
#     ('Mãe', '12355-6789', 1),
#     ('Pai', '12345-6689', 1),
#     ('Vô', '12345-7789', 1),
# )

# contatos_SQL = 'INSERT INTO contatos (nome, tel, grupo_id) VALUES (%s, %s, %s)'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(grupos_SQL, grupos)
        # cursor.executemany(contatos_SQL, contatos)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')

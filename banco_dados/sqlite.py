from sqlite3 import connect, ProgrammingError, Row

tabela_grupos = """
    CREATE TABLE IF NOT EXISTS grupos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao VARCHAR(30)
    )
"""

tabela_contatos = """
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(50),
        tel VARCHAR(40),
        grupo_id INTEGER,
        FOREIGN KEY (grupo_id) REFERENCES grupos(id)
    )
"""

insert_grupos = 'INSERT INTO grupos (descricao) VALUES (?)'
select_grupos = 'SELECT id, descricao FROM grupos'
insert_contatos = 'INSERT INTO contatos (nome, tel, grupo_id) VALUES (?, ?, ?)'
select = """
    SELECT grupos.descricao AS grupo, 
    contatos.nome AS nome
    FROM contatos
    INNER JOIN grupos ON contatos.grupo_id = grupos.id
    ORDER BY grupo, nome
"""

try:
    conexao = connect(':memory:')
    conexao.row_factory = Row

    cursor = conexao.cursor()
    cursor.execute(tabela_grupos)
    cursor.execute(tabela_contatos)

    cursor.executemany(insert_grupos, (('Casa',), ('Amigos',), ('Meu amor',)))
    cursor.execute(select_grupos)
    grupos = {row['descricao']: row['id'] for row in cursor.fetchall()}
    print(grupos)

    contatos = (
        ('Mãe', '123', grupos['Casa']),
        ('Pai', '456', grupos['Casa']),
        ('Juliana', '123', grupos['Meu amor']),
        ('Jusinha', '456', grupos['Meu amor']),
        ('JP', '123', grupos['Amigos']),
        ('Vini', '456', grupos['Amigos']),
        ('sla', '123', None)
    )
    cursor.executemany(insert_contatos, contatos)

    cursor.execute(select)
    for contato in cursor:
        print(f'{contato["nome"]}: {contato["grupo"]}')

except ProgrammingError as e:
    print(f'Erro: {e.msg}')
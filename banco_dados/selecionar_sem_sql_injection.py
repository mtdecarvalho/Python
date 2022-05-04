from bd import nova_conexao

sql = "SELECT * FROM contatos WHERE nome LIKE %s"

with nova_conexao() as conexao:
    nome = input('Contato a localizar: ')
    args = (f'%{nome}%', )
    cursor = conexao.cursor()
    cursor.execute(sql, args)

    for x in cursor:
        print(x)

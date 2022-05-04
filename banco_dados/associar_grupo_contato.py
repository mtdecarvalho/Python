from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

selecionar_grupo = 'SELECT id FROM grupos WHERE descricao = %s'
atualizar_contato = 'UPDATE contatos SET grupo_id = %s WHERE nome = %s'

contato_grupo = {
    'Juliana': 'Minha mulher',
    'Jusinha': 'Minha mulher',
    'Ju': 'Minha mulher',
    'Meu amor': 'Minha mulher',
    'Minha linda': 'Minha mulher',
    'Minha Jusinha': 'Minha mulher',
    'Tetheus': 'Casa',
    'Jujusinha': 'Minha mulher',
    'Matheus': 'Casa',
    'Mãe': 'Casa',
    'Pai': 'Casa',
    'JP': 'Amigos',
    'Vini': 'Amigos'
}

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        for contato, grupo in contato_grupo.items():
            cursor.execute(selecionar_grupo, (grupo,))
            grupo_id = cursor.fetchone()[0]
            cursor.execute(atualizar_contato, (grupo_id, contato))
            conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('Contatos associados')

from mysql.connector import connect
from contextlib import contextmanager

parametros = dict(
    host='localhost',
    port=3306,
    user='root',
    passwd='y62fSiko&Q50',
    database='agenda'
)


@contextmanager
def nova_conexao():
    conexao = connect(**parametros)
    try:
        yield conexao
    finally:
        if (conexao and conexao.is_connected()):
            conexao.close()
            print('finally...')

# usando decorator na função contextmanager, fazemos a adaptação da mesma para ser utilizada para a abertura de uma conexão valida com o bd.
# isto facilita muito a abertura e fechamento da conexao, pois para fazer o mesmo usaremos a função with, que foi utilizada para abrir um arquivo .txt
# apenas alteramos sua lógica para que funcione com um BD de forma semelhante.

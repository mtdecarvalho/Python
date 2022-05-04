from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='y62fSiko&Q50'
)

cursor = conexao.cursor()
# CREATE DATABASE IF NOT EXISTS
cursor.execute('CREATE DATABASE agenda')

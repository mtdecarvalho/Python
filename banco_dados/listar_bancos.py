from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='y62fSiko&Q50'
)

cursor = conexao.cursor()
cursor.execute('SHOW DATABASES')

for i, database in enumerate(cursor, start=1):
    print(f'Banco de dados {i}: {database[0]}')

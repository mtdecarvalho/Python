try:
    from mysql import connector
except ModuleNotFoundError:
    print('MySQL Connector não está instalado!')
else:
    print('MySQL Connector está instalado e pronto!')

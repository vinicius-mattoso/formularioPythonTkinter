'''

Aqui será criado o banco de dados utilizado na aplicação, assim como todas as funções necessárias para acesso e modificação do banco.

'''

# importando libs
import sqlite3 as lite
import os

database_file = 'dados.db'

# Check if the database file exists
if os.path.exists(database_file):
    # If the file exists, establish a connection to the existing database
    con = lite.connect(database_file)
else:
    # If the file doesn't exist, create a new database file and establish a connection
    con = lite.connect(database_file)




# # Criando a concexão com o banco de dados
# con = lite.connect('dados.db')

# cirando uma tabela no banco de dados
with con:
    cur = con.cursor()
    '''
      todo comando em SQL é em maiúsculo
      em minusculo é o nome da tabela
      dentro dele vão ser as colunas das tabelas
    '''
    cur.execute("CREATE TABLE formulario (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, dia_em DATE, estado TEXT, assunto TEXT)")
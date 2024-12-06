
import sqlite3 
#IMPORTA A BIBILIOTECA
 
conexao = sqlite3.connect('exemplo.db')

#Cria um banco de dados SQLite chamado exemplo.db (ou o abre, se já existir).


cursor = conexao.cursor()
 #Um cursor é um objeto que permite executar comandos SQL no banco de dados. Ele funciona como um intermediário entre o Python e o banco de dados.
 
cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
''')        
#.Cria uma tabela chamada alunos com três colunas: id, nome e idade.


cursor.execute('INSERT INTO alunos (nome, idade) VALUES ("João Silva", 20)')
cursor.execute('INSERT INTO alunos (nome, idade) VALUES ("Maria Santos", 22)')
#.Insere dois registros na tabela alunos: um para "João Silva" e outro para "Maria Santos".


#O comando commit() confirma todas as alterações feitas no banco de dados desde a ultima confirmação (o que inclui a inserção dos registrosV
conexao.commit()
 

# Consulta os registros da tabela 'alunos'
print("Alunos:")
cursor.execute('SELECT * FROM alunos')
resultados_alunos = cursor.fetchall()
for aluno in resultados_alunos:
    print(aluno)



cursor.execute('SELECT * FROM alunos')
resultados = cursor.fetchall()
 
for aluno in resultados:
    print(aluno)
 
#4.Consulta todos os registros da tabela alunos e imprime cada um deles.


conexao.close()
#Depois de terminar todas as operações no banco de dados, o código fecha a conexão com o banco de dados.


#depois Fecha a conexão com o banco de dados.

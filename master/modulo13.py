import pyodbc

# Definindo a string de conexão
conn_str = r'DRIVER={SQL Server Native Client 11.0};' \
           r'SERVER=(localdb)\MSSQLLocalDB;' \
           r'DATABASE=NomeDoSeuBancoDeDados;' \
           r'Trusted_Connection=yes;'

#A Estabelecendo a conexão
try:
    conn = pyodbc.connect(conn_str)
    print("Conexão bem-sucedida!")
    
    cursor = conn.cursor()

    # Aqui você pode consultar a tabela
    cursor.execute('SELECT * FROM sua_tabela')
    
    for row in cursor.fetchall():
        print(row)

except Exception as e:
    print("Erro ao conectar:", e)

finally:
    # Fechando a conexão
    if conn:
        conn.close()import pyodbc

# Definindo a string de conexão
conn_str = r'DRIVER={SQL Server Native Client 11.0};' \
           r'SERVER=(localdb)\MSSQLLocalDB;' \
           r'DATABASE=NomeDoSeuBancoDeDados;' \
           r'Trusted_Connection=yes;'

# Estabelecendo a conexão
try:
    conn = pyodbc.connect(conn_str)
    print("Conexão bem-sucedida!")
    
    cursor = conn.cursor()

    # Aqui você pode executar consultas
    cursor.execute('SELECT * FROM sua_tabela')
    
    for row in cursor.fetchall():
        print(row)

except Exception as e:
    print("Erro ao conectar:", e)

finally:
    # Fechando a conexão
    if conn:
        conn.close()
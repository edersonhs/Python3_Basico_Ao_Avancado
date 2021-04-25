import sqlite3

# Criando conexão com o arquivo de dados
conexao = sqlite3.connect(
    './aulas/Base_de_Dados_com_Python-SQLite-MySQL-e-MariaDB/SQLite-Usando_o_modulo_SQLite3/database.db')
cursor = conexao.cursor()   # Vai executar os comandos sql dentro da database

# Criar tabela
cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')

# Inserindo dados em uma tabela
# Para Prevenir SQL Injection passamos os dados pela tupla
cursor.execute(
    'INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 50))

# Exemplo 2 - Passar os dados por dicionarios
cursor.execute(
    'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
    {'nome': 'João', 'peso': 45})

# Exemplo 3 - Omitir os campos que estão sendo preenchidos
cursor.execute(
    'INSERT INTO clientes VALUES (:id, :nome, :peso)',
    {'id': None, 'nome': 'Daniel', 'peso': 113})

# Exemplo 4 - NSFW (Risco de SQL Injection)
cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("Lucas", 90.3)')
conexao.commit()   # Executar o que consta no cursor

# Alterando dados de uma tabela
cursor.execute('UPDATE clientes SET nome = ? WHERE id=?', ('Thiago', 2))
conexao.commit()

# Deletando dados de uma tabela
cursor.execute('DELETE FROM clientes WHERE id=?', (1, ))
conexao.commit()

# Select para mostrar todo o conteudos da tabela de clientes
cursor.execute('SELECT * FROM clientes')
# Select mais especifico: "SELECT nome, peso, FROM clientes WHERE peso > 50"

# cursor.fetchall() - Trás todos os valores do select em um iteravel
for linha in cursor.fetchall():
    identificador, nome, peso = linha   # Desempacotando os dados
    print(identificador, nome, peso)

# Sempre que temos um Cursor e uma Conexão é uma boa praticar fechar os mesmos
# quando tiver terminado de usar, portanto:
cursor.close()
conexao.close()

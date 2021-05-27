import pymysql.cursors
from contextlib import contextmanager

# CRUD - Create, Read, Update, Delete


@contextmanager
def conecta():   # criando um gerenciados de contexto para automatizar o fechamento da conexão com o banco de dados
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',   # Pode ser omitido, desde que as operações sejam especificas para a base de dados correta
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor   # Agrupando as informações em dicionários
    )

    try:
        yield conexao   # retorna a conexão para ser utilizada no with
    finally:
        conexao.close()


# Inserindo um único registro
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
#         cursor.execute(sql, ('Jack', 'Monroe', 112, 220))
#         conexao.commit()

# ////////////////////////////////////////////////////////////////////////////////////////////////

# Inserindo vários registros simultaneamente
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
#
#         dados = [
#             ('Muriel', 'Figueiredo', 19, 55),
#             ('Rose', 'Andrade', 42, 52),
#             ('Jose', 'Fonseca', 16, 69),
#         ]
#
#         cursor.executemany(sql, dados)
#         conexao.commit()

# ////////////////////////////////////////////////////////////////////////////////////////////////

# Excluindo um registro da tabela
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (6,))
#         conexao.commit()

# ////////////////////////////////////////////////////////////////////////////////////////////////

# Excluindo vários registro da tabela
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
#         cursor.execute(sql, (7, 8, 9))
#         conexao.commit()

# ////////////////////////////////////////////////////////////////////////////////////////////////

# Excluindo registros em um range (no exemplo, entre 10 e 12)
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         cursor.execute(sql, (10, 12))
#         conexao.commit()

# ////////////////////////////////////////////////////////////////////////////////////////////////

# Alterando um registro
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
#         cursor.execute(sql, ('Joana', 5))
#         conexao.commit()

# ////////////////////////////////////////////////////////////////////////////////////////////////

# Lendo os dados
with conecta() as conexao:   # Fecha a conexão
    with conexao.cursor() as cursor:   # Fecha o cursor
        # Quando o db não é informado informar além da tabela a base de dados
        cursor.execute('SELECT * FROM clientes ORDER BY id DESC LIMIT 100')
        '''
        SELECT nome as n, sobrenome as sn - apelidando nome de n e sobrenome de sn
        FROM clientes.clientes - especificando database e tabela
        ORDER BY id DESC - ordendando por id de maneira decrescente (ASC para ordem crescente)
        LIMIT 100  - limitando o select a 100 elementos por questões de desempenho
        '''
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)

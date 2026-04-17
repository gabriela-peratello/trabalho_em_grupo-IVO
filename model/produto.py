from database.conexao import conectar

# Recuperar produtos, trazer do banco de dados
def recuperar_produtos():
    conexao, cursor = conectar()

    cursor.execute("SELECT codigo, produto, descr, preco, foto FROM produtos;")
    resultado = cursor.fetchall()

    conexao.close()

    return resultado
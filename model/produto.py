from database.conexao import conectar

# Recuperar produtos, trazer do banco de dados
def recuperar_produto():
    conexao, cursor = conectar()
    # Executando a consulta nos produtos
    cursor.execute("SELECT codigo, produto, descr, preco, foto FROM produtos;")

    # Recuperando os dados dos produtos
    resultado = cursor.fetchall()

    # Fechando a conexão
    conexao.close()

    return resultado


 
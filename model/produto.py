from database.conexao import conectar

# Recuperar produtos, trazer do banco de dados
def recuperar_produtos():
    conexao, cursor = conectar()

    cursor.execute("SELECT codigo, produto, descr, preco, foto FROM produtos;")
    resultado = cursor.fetchall()

    conexao.close()

    return resultado


def rec_destq():
    conexao, cursor = conectar()
    cursor.execute("""
        SELECT codigo, foto FROM produtos WHERE destaque = 1
                """)
    
    resultado = cursor.fetchall()
    conexao.close()
    return resultado
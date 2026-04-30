from database.conexao import conectar

def recuperar_carrinho(usuario: str) -> list:
    conexao, cursor = conectar()
    cursor.execute("""
       SELECT 
            carrinhos.cod_car,
            carrinhos.usuario,
            carrinhos.data_criacao,
            carrinhos.finalizado,
            produtos.produto,
            itens_carrinhos.quantidade,
            produtos.preco,
            produtos.foto
        FROM carrinhos
        INNER JOIN itens_carrinhos ON carrinhos.cod_car = itens_carrinhos.cod_car
        INNER JOIN produtos ON produtos.codigo = itens_carrinhos.cod_produto
        WHERE carrinhos.usuario = %s;
    """, [usuario])
    resultado = cursor.fetchall()
    conexao.close()
    return resultado
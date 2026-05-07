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



def inserir_item(usuario, cod_produto, quantidade = 1):
    conexao, cursor = conectar()
    cursor.execute(""" 
        SELECT cod_car FROM carrinhos WHERE usuario = %s AND finalizado = 0 LIMIT 1;              
        """, [usuario])
    
    resultado_carrinho = cursor.fetchone()

    if resultado_carrinho:
        cod_carrinho = resultado_carrinho["cod_car"]
    else:
        cursor.execute("""
                    INSERT INTO carrinhos (usuario)
                    VALUES (%s)
                        """, [usuario])
        cod_carrinho = cursor.lastrowid

    cursor.execute("""
        INSERT INTO itens_carrinho
            (cod_car, cod_produto, quantidade )
        VALUES
            (%s, %s, %s)
            """, [cod_carrinho, cod_produto, quantidade])

    conexao.commit()
    conexao.close()

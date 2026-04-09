import mysql.connector

def conectar():
    # Conectando no banco de dados
    conexao = mysql.connector.connect(
        host ="127.0.0.1",
        port = 3306,
        user = "root",
        password = "root",
        database = "devbg"
    )

    cursor = conexao.cursor(dictionary=True)
    return conexao, cursor
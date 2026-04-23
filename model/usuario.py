from database.conexao import conectar

class Usuario:
    def __init__(self, usuario:str, senha:str, nome:str=None):
        self.usuario = usuario
        self.senha = senha
        self.nome = nome 

    def cadastrar(self):
        conexao, cursor = conectar()
        cursor.execute("""
                    INSERT INTO usuarios (usuario, senha, nome)
                    VALUES (%s, %s, %s);
                    """, [self.usuario, self.senha, self.nome])
        conexao.commit()
        conexao.close()

    # Ou usar staticmethod ou self, não da pra usar os dois
    @staticmethod
    def logar(usuario:str, senha:str) -> dict:
        conexao, cursor = conectar()

        cursor.execute(""" SELECT usuario, senha FROM devbg.usuarios WHERE usuario = %s and senha = %s
                       """,
                    (usuario, senha))
        
        resultado = cursor.fetchone()
        conexao.close()

        return resultado


from flask import Flask, redirect, render_template, request
from model.produto import recuperar_produto
from model.usuario import Usuario

app = Flask(__name__)

@app.route("/")
def pag_inicial():
    produtos = []
    return render_template("index.html", produtos=produtos)

@app.route("/produto/<codigo>")
def pag_dois(codigo):
    try:
        produto = recuperar_produto(codigo)

        if not produto:
            return "Produto não encontrado", 404

        return render_template("produto.html", produto=produto)

    except Exception as e:
        return f"Erro: {e}"
    

@app.route("/cadastrar_usuario", methods= ["POST"])
def cadastrar_usuario():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    nome = request.form.get("nome")

    novo_usuario = Usuario(usuario, senha, nome)
    novo_usuario.cadastrar()

    return redirect("/")

@app.get("/cadastro")
def cadastro_login():
    return render_template("cadastro.html")










if __name__ == "__main__":
    app.run(debug=True)
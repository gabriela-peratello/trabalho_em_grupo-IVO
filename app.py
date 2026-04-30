from flask import Flask, jsonify, redirect, render_template, request, session
from model.carrinho import recuperar_carrinho
from model.produto import recuperar_produtos
from model.usuario import Usuario

app = Flask(__name__)

@app.route("/")
def pag_inicial():
    produtos = recuperar_produtos()
    return render_template("index.html", produtos=produtos)

@app.route("/logar")
def login():
    return render_template("login.html") 

@app.route("/produto/<codigo>")
def pag_dois(codigo):
    produto = recuperar_produtos(codigo)

    return render_template("produto.html", produto = produto)


@app.route("/cadastrar_usuario", methods=["POST"])
def cadastrar_usuario():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    nome = request.form.get("nome")

    novo_usuario = Usuario(usuario, senha, nome)
    novo_usuario.cadastrar()

    return redirect("/")


@app.route("/logar/usuario", methods = ["POST"])
def logar_usuario():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    resultado = Usuario.logar(usuario, senha)

    if resultado:
        session["usuario_logado"] = resultado
        return redirect("/")
    else:
        return "Erro"

    

@app.route("/api/get/carrinho", methods = ["GET"])
def api_carrinho(): 
    if "usuario_logado" in session:
        usuario = session["usuario_logado"]["usuario"]
        carrinho = recuperar_carrinho(usuario)
        return jsonify(carrinho), 200
    else:
        return jsonify({"message":"Usuário não logado."}), 401



@app.get("/cadastro_login")
def cadastro_login():
    return render_template("cadastro.html")


if __name__ == "__main__":
    app.run(debug=True)
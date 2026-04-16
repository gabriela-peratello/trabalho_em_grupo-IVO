from flask import Flask, render_template
from model.produto import recuperar_produto

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

if __name__ == "__main__":
    app.run(debug=True)
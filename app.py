from flask import Flask, render_template
from model.produto import recuperar_produto

app = Flask(__name__)

@app.route("/")
def pag_inicial():
    return render_template("index.html, produtos = produtos")

@app.route("/produto")
def pag_dois():
    return render_template("card.html")


app.run()


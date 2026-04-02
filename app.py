from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def pag_inicial():
    return render_template("index.html")

@app.route("/produto")
def pag_dois():
    return render_template("card.html")


app.run()


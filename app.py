from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def pag_inicial():
    return render_template("index.html")

@app.route("/pagina2")
def pag_dois():
    return render_template("layout.html")


app.run()


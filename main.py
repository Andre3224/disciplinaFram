from flask import Flask, make_response
from markupsafe import escape
from flask import render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cad/usuario")
def usuario():
    return render_template('usuario.html', titulo="Cadastro de Usuario")

@app.route("/cad/caduser", methods=['POST'])
def caduser():
    # Aqui você pode tratar os dados e salvar no banco ou exibir uma mensagem
    dados = request.form
    return f"Usuário cadastrado com sucesso: {dados}"

@app.route("/anuncios/perguntas")
def perguntas():
    return 1
@app.route("/anuncios/compra")
def compra():
    return 1

@app.route("/anuncios/venda")
def venda():
    return 1

@app.route("/anuncios/favoritos")
def favoritos():
    return 1

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

if __name__ == "__main__":
    app.run(debug=True)
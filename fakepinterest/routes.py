#criar as rotas do nosso site (os links)
from flask import render_template, url_for
from fakepinterest import app
from flask_login import login_required
from fakepinterest.forms import FormLogin, FormCriarConta


@app.route("/", methods=["GET", "POST"])
def homepage():
    formlogin = FormLogin()
    return render_template("homepage.html", form=formlogin) #form antes do =, é o nome que a variável vai ter no html


@app.route("/criarconta", methods=["GET", "POST"])
def criarconta():
    formcriarconta = FormCriarConta()
    return render_template("criarconta.html", form=formcriarconta)


@app.route("/perfil/<usuario>")  # essa chave <>, sinaliza que é uma variável.
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)

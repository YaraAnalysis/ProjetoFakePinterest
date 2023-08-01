#criar as rotas do nosso site (os links)
from flask import render_template, url_for
from fakepinterest import app, database, bcrypt
from flask_login import login_required
from fakepinterest.forms import FormLogin, FormCriarConta
from fakepinterest.models import Usuario, Foto


@app.route("/", methods=["GET", "POST"])
def homepage():
    form_login = FormLogin()
    return render_template("homepage.html", form=form_login) #form antes do =, é o nome que a variável vai ter no html


@app.route("/criarconta", methods=["GET", "POST"])
def criar_conta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data,
                          email=form_criarconta.email.data, senha=senha)
        database.session.add(usuario) #adicionar usuário
        database.session.commit()  #commitar as infos no banco
    return render_template("criarconta.html", form=form_criarconta)


@app.route("/perfil/<usuario>")  # essa chave <>, sinaliza que é uma variável.
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)

#criar as rotas do nosso site (os links)
from flask import render_template, url_for, redirect
from fakepinterest import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from fakepinterest.forms import FormLogin, FormCriarConta
from fakepinterest.models import Usuario, Foto


@app.route("/", methods=["GET", "POST"])
def homepage():
    form_login = FormLogin()
    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario)
            return redirect(url_for("perfil", id_usuario=usuario.id))
    return render_template("homepage.html", form=form_login)  # form antes do =, é o nome que a variável vai ter no html


@app.route("/criarconta", methods=["GET", "POST"])
def criar_conta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data,
                          email=form_criarconta.email.data, senha=senha)
        database.session.add(usuario)           #adicionar usuário
        database.session.commit()               #commitar as infos no banco
        login_user(usuario, remember=True)      #faz o login após o cadastro
        return redirect(url_for("perfil", id_usuario=usuario.id))
    return render_template("criarconta.html", form=form_criarconta)


@app.route("/perfil/<id_usuario>")         #essa chave <>, sinaliza que é uma variável.
@login_required
def perfil(id_usuario):
    if int(id_usuario) == int(current_user.id):
        # o usuario tá vendo o perfil dele
        return render_template("perfil.html", usuario=current_user)
    else:
        usuario = Usuario.query.get(int(id_usuario))
        return render_template("perfil.html", usuario=usuario)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))

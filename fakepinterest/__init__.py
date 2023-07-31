#definir o nosso app, criar o nosso site
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"  #Aqui pode escolher outro DB, tipo Postgrees
app.config["SECRET_KEY"] = "b405fce2e6d00c927b01de29aa9feeb8"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"

from fakepinterest import routes
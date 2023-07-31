#definir o nosso app, criar o nosso site
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"  #Aqui pode escolher outro DB, tipo Postgrees

database = SQLAlchemy(app)

from fakepinterest import routes

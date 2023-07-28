#definir o nosso app, criar o nosso site

from flask import Flask

app = Flask(__name__)

from fakepinterest import routes

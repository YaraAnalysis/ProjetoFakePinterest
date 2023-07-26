from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "FakePinterest - Meu primeiro site Flask!"

@app.route("/perfil")
def perfil():
    return "Perfil do Usuário"

if __name__ == "__main__":
    app.run(debug=True)

import datetime

from flask import *
from datetime import *

app = Flask(__name__)

nome_dev = 'Rene'

@app.route("/") #decorator
def index():
    return render_template('index.html', valor=nome_dev)


@app.route("/receberNome", methods=["POST"])
def recebi_nome_usuario():
    nome = str(request.form.get('nomeusuario'))
    cargo = str(request.form.get('cargousuario'))
    senha = str(request.form.get('senhausuario'))

    print(nome+" - "+cargo)

    if(nome == senha):
        msg = 'A senha deve ser diferente do seu nome'
        return render_template('index.html', valor=nome_dev, mensagem=msg)
    else:
        return f'deu certo {nome}'





@app.route("/hora")
def minha_pagina():
    data = datetime.now()
    ano = data.year
    mes = data.month
    dia = data.day
    hora = data.hour
    minutos = data.minute
    segundos = data.second

    return f'Hoje, a data é {dia}-{mes}-{ano} e a hora é {hora}:{minutos}:{segundos}'

if(__name__ == '__main__' ):
    app.run(debug=True)
'''
https://github.com/renegadelhaedu/introwebflask.git
'''

import datetime

from flask import *
from datetime import *

app = Flask(__name__)

usuarios = ['adm']

nome_dev = 'Rene'

@app.route("/") #decorator
def index():
    return render_template('index.html', valor=nome_dev)


@app.route("/receberNome", methods=["POST"])
def recebi_nome_usuario():
    nome = str(request.form.get('nomeusuario'))
    cargo = str(request.form.get('cargousuario'))
    senha = str(request.form.get('senhausuario'))

    usuarios.append(nome)

    listao = ''
    for user in usuarios:
        listao = listao + '\n' + user

    print(listao)

    if(nome == senha):
        msg = 'A senha deve ser diferente do seu nome'
        return render_template('index.html', valor=nome_dev, mensagem=msg)
    else:
        return render_template('sucessocadastro.html',lista=listao)



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
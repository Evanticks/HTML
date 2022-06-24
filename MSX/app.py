#Importamos os para poder utilizar os.environ
import os
from flask import Flask, render_template, request
app = Flask(__name__)
from misfunciones import buscar

import json
with open("static/MSX.json") as fichero:
    datos=json.load(fichero)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/juegos')
def juegos():
    return render_template("juegos.html")


@app.route('/lista_juegos',methods=["POST"])
def lista_juegos():
    texto=request.form.get("texto")
    juegos=buscar(texto)
    for juego in juegos:
        if juego.get("id") == 1:
            return render_template("lista_juegos.html",juegos=datos)
        else:
            return render_template("lista_juegos.html",juegos=juegos)



@app.route('/juego/<id>')
def juego(id):
    for dato in datos:
        if dato.get("id") == int(id):
            return render_template("juego.html",dato=dato)


port=os.environ["PORT"]
app.run('0.0.0.0',int(port),debug=False)
#app.run("0.0.0.0",5000,debug=True)
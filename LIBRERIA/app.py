import os
from flask import Flask, render_template, request, abort
app = Flask(__name__)
import json
with open("static/books.json") as fichero:
    datos=json.load(fichero)

@app.route('/')
def inicio():
    nombre=[]
    for libro in datos:
        diccionario={"title":libro.get("title"),"isbn":libro.get("isbn")}
        nombre.append(diccionario)
    return render_template("inicio.html",nombre=nombre)
    

@app.route('/libro/<isbn>')
def libro(isbn):
    detalles=[]
    error=False
    for libro in datos:
        if libro.get("isbn") == isbn:
            diccionario={"title":libro.get("title"),"isbn":libro.get("isbn"),"pageCount":libro.get("pageCount"),"authors":libro.get("authors"),"categories":libro.get("categories"),"thumbnailUrl":libro.get("thumbnailUrl"),"status":libro.get("status")}
            detalles.append(diccionario)
            print(diccionario)
            error=True
    if error == False:
        return abort (404) 
    return render_template("libro.html",detalles=detalles)

app.run("0.0.0.0",5000,debug=True)
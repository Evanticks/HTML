import json
with open("static/MSX.json") as fichero:
    datos=json.load(fichero)

#class mydict(dict):
#    def __getitem__(self, value):
#        keys = [k for k in self.keys() if value in k]
#        key = keys[0] if keys else None
#        return self.get(key)
#juegos=[]
#def conversion(texto):
#    juegos=[]
#    for dato in datos:
#        result=mydict(dato)
#        select=[result['nombre'],result['categoria']]
#        #debemos convertir esta lista en cadena para el starstwith, se realiza con join
#        cadena = ','.join(str(v) for v in select)
#        if cadena.startswith(texto):
#            juegos.append(cadena)
#    return juegos

def buscar (texto):
    juegos=[]
    for dato in datos:
        nombre=str(dato.get("nombre"))
        if nombre.startswith(texto):
            diccionario={"nombre":dato.get("nombre"),"desarrollador":dato.get("desarrollador"),"id":dato.get("id")}
            juegos.append(diccionario)
            return juegos

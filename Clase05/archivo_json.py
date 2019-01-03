import json
dato = ""
with open('prueba.json') as file:
    dato = json.load(file)
print(dato['nombres'])
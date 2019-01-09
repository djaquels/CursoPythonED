lista = [1,2]
try:
    print(lista[10])
except IndexError:
    print("Indice Fuera De Rango")
#No se cierra la aplicacion
print("Adios")
try:
    print(10/0)
except ZeroDivisionError: # Manejo de errores especificos
    print("Division Invalida")
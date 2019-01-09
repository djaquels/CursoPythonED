try:
    print(10/0)
except ZeroDivisionError: # Manejo de errores especificos
    print("Division Invalida")
else: #Continua con el proceso del programa
    print("Sin errores")
finally:
    print("Adios")
# Tuplas
tupla1 = (1,2,3,4,5) #del mismo tipo
tupla2 = ('aaa','aabb','abba') #del mismo tipo: cadenas
tupla3 = (1,'aaaa',True,4.5) #de diferentes tipos
print(tupla3[2])
#Ejemplo Uso De Tuplas
def enviar_datos():
    nombre = 'Martinolli'
    correo = 'cmartinolli@gmail.com'
    edad = 30
    ciudad = 'CDMX'
    return (nombre,correo,edad,ciudad)
def recibir_datos(datos):
    print(datos[0])
    print(datos[1])
    print(datos[2])
datos = enviar_datos()
recibir_datos(datos)
# Listas
# Diccionarios
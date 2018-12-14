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
#si se pueden modificar
lista = [1,2,3,4,5,6]
lista1 = [1,"c",1.2,True]
lista[0] = 0
print(lista)
for elemento in lista:
    print(elemento) #recorremos la lista
lista.append(1000)
print(lista)
lista.pop() # se borra el ultimo elemento
#unir listas
l = [10,100,1000]
l2 = [20,200,2000]
l.extend(l2)
print(l)
del l[0]
print(l)
l.remove(20) # borra elemento que coincida con 20
print(l)
l.sort() # ordena lista
l.sort(reverse=True) #ordena inversamente
print(l[-2]) # indice negativos
# Diccionarios
jugadores = {'Javier Hernandez':'West Ham','Raul Jimenez':'Wolverhampton','Hirving Lozano':'PSV'}
print(jugadores['Javier Hernandez'])
for j in jugadores:
    print(j)

diccionario = {'a':(1,2),'b':(3,4),'c':(5,6)} #tipos compuestos
print(diccionario.values()) #obtiene los valores
print(diccionario.keys()) # obtiene las llaves
nuevo = diccionario.copy() # copia el diccionario
diccionario.clear() # borra los datos del diccionario
nuevos = {'Diego Lainez':'America','Raul Gudiño':'Guadalajara'}
jugadores.update(nuevos)
print(jugadores)

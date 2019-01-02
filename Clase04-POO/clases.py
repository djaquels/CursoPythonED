class Persona:
    nombre = ""
    edad = 0
    pais = ""
    contactos = {}
    #constructor
    def __init__(self,nombre,edad,pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais

    def saludar(self):
        print("hola mi nombre es:",self.nombre)
    def añadir_contacto(self,nombre,telefono):
        print("Nuevo contacto")
        t = {nombre:telefono}
        self.contactos.update(t)
        print(self.contactos)


pepito = Persona("Hirving",23,"MX")
print(pepito.edad)
pepito.saludar()
pepito.añadir_contacto("Juan","55698741")
pepito.añadir_contacto("Manuel","6589653")
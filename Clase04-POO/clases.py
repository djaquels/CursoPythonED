class Persona:
    nombre = ""
    edad = 0
    pais = ""
    contactos = {}
    def saludar(self):
        print("hola mi nombre es:",self.nombre)
    def añadir_contacto(self,nombre,telefono):
        print("Nuevo contacto")
        t = {nombre:telefono}
        self.contactos.update(t)
        print(self.contactos)


pepito = Persona()
print(pepito.edad)
pepito.saludar()
pepito.añadir_contacto("Juan","55698741")
pepito.añadir_contacto("Manuel","6589653")
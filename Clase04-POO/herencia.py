class Magico:
    nombre = ""
    edad = 0 
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print("Hola Mi Nombre Es ", self.nombre)

class Mago(Magico):#Asi se hereda de la clase Magico 
    casa = ""
# Python soporta la herencia multiple
harry = Mago("Harry",18)
harry.saludar()
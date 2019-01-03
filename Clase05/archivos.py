#Crear archivos
archivo = open('datos.txt','w')
archivo.close()
def escribir_archivo():
    archivo = open('datos.txt','a')
    archivo.write("Héctor Jacales\n")
    archivo.write("u.u\n")
def leer_archivo():
    archivo = open('datos.txt','r')
    linea = archivo.readline()
    while(linea != ""):
        print(linea)
        linea = archivo.readline()
escribir_archivo()
leer_archivo()
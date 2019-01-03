import csv
doc_csv = open('prueba.csv','w')
csv_data = csv.writer(doc_csv)
lista= [["Jose",999999],["Layun",7777]]
for elemento in lista:
    csv_data.writerow(elemento)
doc_csv.close()

#Para leer
doc2 = open('prueba.csv','r')
documento = csv.reader(doc2)
for(nombre,numero) in documento:
    print(nombre,numero)
doc2.close()
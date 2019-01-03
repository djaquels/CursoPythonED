from xml.etree.ElementTree import parse
doc = parse('prueba.xml')

for elemento in doc.findall('nombre'):
    print(elemento.text)
import re

patron = re.compile("[A-Z]\d")
print(patron.search("sdadasddaA4"))
if(re.search("[A-Z][0-9].*","A0sadasda")):
    print("id valido")

#para reemplazar
print(re.sub(r"[a-z]","Simpson","hola"))
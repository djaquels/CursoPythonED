#Expresiones regulares en Python
import re

print(re.search(r"g","parangaticutirimicuaro"))
patron = re.compile("\d\d")
print(patron.search("asdad1sadsad4adad78"))
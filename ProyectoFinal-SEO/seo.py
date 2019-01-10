#Auditoria SEO a PYTHON.ORG Y HEPTORSJ.GITHUB.IO

#imports
import os
import re
import urllib.request as request
from urllib.request import urlopen
from bs4 import BeautifulSoup
#****verifircar https****
req = request.Request('http://heptorsj.github.io/')
res = request.urlopen(req)
#Verificar HTTPS
if(re.search("https.*",res.geturl())):
    print("Tiene HTTPS")
else:
    print("No Tiene HTTTPS")
#**** Peso De La Pagina
url = "http://heptorsj.github.io/"
print("url:",url)
site = request.urlopen(url)
meta = site.info()
print("Content-Length:",site.headers['content-length'])
#Comparando en disco
f = open("out.html","wb")
f.write(site.read())
site.close()
f.close()
print("os.stat().st_sizes returns",os.stat("out.html").st_size)
f = open("out.html","r")
print("File On Disk After Download: ", len(f.read()))
f.close()
#Verificar www
patron = re.compile("www")
if(patron.search(res.geturl())):
    print("Tiene WWW")
else:
    print("No Tiene WWW")
#Meta Description
try:
    site = request.urlopen("https://heptorsj.github.io/")
    soup = BeautifulSoup(site)
    desc = soup.find('meta',attrs={'name':'description'})
    l = len(desc.get('content'))
    print("Tamaño De Descripcion es: ",l)
    if l > 154 :
        print("No cumple con los estandares")
    else:
        print("Cumple Con Los Estandares")
except Exception:
    print("Error Leyendo URL")
#****Verificar etiqueta titulo****
html = urlopen('https://heptorsj.github.io/')
soup = BeautifulSoup(html.read())
print("El tamaño de title es",len(soup.html.head.title.string))
print("El title dice",soup.html.head.title.string)
#*** Palabras Claves ***
site = request.urlopen('https://python.org')
soup = BeautifulSoup(site)
keywords = soup.find('meta',attrs={'name':'keywords'})
print("keywods:" ,keywords.get('content'))
words = keywords.get('content').split()
for word in words:
    print(word,len(soup.findAll(text=re.compile(word))))
#*** ALT en imagenes *** 
site = request.urlopen("https://heptorsj.github.io/")
soup = BeautifulSoup(site)
count = 1
for image in soup.findAll('img'):
    print("Imagen #{}".format(count),image["src"])
    print("Alt de Imagen:" , image.get("alt","None"))
    count += 1
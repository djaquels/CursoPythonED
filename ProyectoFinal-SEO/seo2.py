#AUDITORIA SEO COMPLEMENTO
import os
import re
import urllib.request as request
from urllib.request import urlopen
from bs4 import BeautifulSoup
#https://heptorsj.github.io/ otro ejemplo https://python.org
#*** H1 ***
site = request.urlopen("https://heptorsj.github.io/")
soup = BeautifulSoup(site)
for h1 in soup.find_all('h1'):
    print("Este es un h1" ,h1)
print("En total son {}".format(len(soup.find_all('h1'))))

#*** ENLACES ROTOS
site = request.urlopen("https://python.org")
soup = BeautifulSoup(site)
links = []
elements = soup.select('a')
for element in elements:
    link = element.get('href')
    if(link.startswith('http')):
        links.append(link)
print(links)
links = []
for l in links[:10]:
    petition = urlopen(l)
    print("Enlace", l ,"Respuesta: ",petition.code)
### **** ROBOTS.TXT *** 
try:
    for file in os.listdir('/home'):
        if(file.endswith('.txt')):
            print("Se encontro el archivo robots en: " ,os.path.join())
except Exception:
    print("Error Leyendo")
### *** FAVICON ***
url = "https://python.org"
page = request.urlopen(url)
soup = BeautifulSoup(page)
icon_link = soup.find('link',rel="icon")
icon = request.urlopen(url+icon_link['href'])
with open("test.icon","wb") as f:
    try:
        f.write(icon.read())
        print("Succces")
    except:
        print("No hay ICONO")
#*** ANALITYCS ***
site = request.urlopen("https://python.org")
soup = BeautifulSoup(site)
if(soup.findAll(text=re.compile(".google-analytics"))):
    print("Tiene GOOGLE ANALYTICS")
else:
    print("No Tiene Analytics")
#*** ETIQUETAS META *** 
# IDIOMA
site = request.urlopen("https://python.org")
soup = BeautifulSoup(site,'html.parser')
lang = soup.find('html')['lang']
print("El idioma del sitio es: " , lang)
#CHARSET 
site = "https://python.org"
print("pagina: ", site)
peticion = request.urlopen(site)
meta = peticion.info()
print("Content Type: ")
### VIEWPORT
site = request.urlopen("https://python.org")
soup = BeautifulSoup(site)
if(soup.find('meta',attrs={'name':'viewport'})):
    print("Viewport: ",soup.find('meta',attrs={'name':'viewport'}) )
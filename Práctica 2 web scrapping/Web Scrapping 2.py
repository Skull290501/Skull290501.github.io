import requests
from bs4 import BeautifulSoup
import pandas as pd

def obtenerDatos(url):
    pagina = requests.get(url)
    sopa = BeautifulSoup(pagina.content, 'lxml')
    
    artistaElemento = sopa.find('dd', itemprop='creator')
    artista = artistaElemento.a.text.strip() if artistaElemento and artistaElemento.a else "N/A"
    titulo = sopa.find('dd', itemprop='name').span.text.strip()
    lugar = sopa.find('dd', itemprop='locationCreated').span.text.strip()
    fecha = sopa.find('dd', itemprop='dateCreated').span.text.strip()
    dimension = sopa.find('dd', itemprop='size').span.text.strip()
    
    return artista, titulo, lugar, fecha, dimension

# Enlaces
enlaces = [
    'https://www.artic.edu/artworks/40619/zapata',
    'https://www.artic.edu/artworks/21656/the-flag',
    'https://www.artic.edu/artworks/49614/zapatistas'
]

# Crear primer archivo CSV
titulos = [enlace.split('/')[-1] for enlace in enlaces]
datosTitulos = {
    'ColeccionOrozco': titulos,
    'Enlace': enlaces
}
dfTitulos = pd.DataFrame(datosTitulos)
dfTitulos.to_csv('C:/Users/yeyos/OneDrive/Documentos/pinturas.csv', index=False, encoding='latin1')

# Crear segundo archivo CSV
detalles = {
    'Artista': [],
    'Titulo': [],
    'Lugar': [],
    'Fecha': [],
    'Dimension': [],
    'Enlace': []
}

for enlace in enlaces:
    artista, titulo, lugar, fecha, dimension = obtenerDatos(enlace)
    detalles['Artista'].append(artista)
    detalles['Titulo'].append(titulo)
    detalles['Lugar'].append(lugar)
    detalles['Fecha'].append(fecha)
    detalles['Dimension'].append(dimension)
    detalles['Enlace'].append(enlace)

dfDetalles = pd.DataFrame(detalles)
dfDetalles.to_csv('C:/Users/yeyos/OneDrive/Documentos/pinturasDetalles.csv', index=False, encoding='latin1')

print("Archivos CSV creados con éxito\n")

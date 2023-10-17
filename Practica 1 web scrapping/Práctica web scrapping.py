import requests
from bs4 import BeautifulSoup
import csv

def MercadoLibre(soup):
    return soup.find('span', {'class' : 'andes-money-amount__fraction'}).getText()

def RadioShack(soup):
    return soup.find('span', {'id' : 'price1'}).getText()

def Cyberpuerta(soup):
    return soup.find('span', {'class':'priceText'}).getText()

def obhtml(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, "html.parser")

ML = obhtml('https://www.mercadolibre.com.mx/sony-playstation-5-825gb-standard-color-blanco-y-negro/p/MLM16171888?pdp_filters=category:MLM167860#searchVariation=MLM16171888&position=1&search_layout=stack&type=product&tracking_id=96846cde-58c5-48c5-ad28-fe929b028303')
RS = obhtml('https://www.radioshack.com.mx/store/Categoría/Todas/Gamers-y-Descargables/PlayStation/Consolas/Consola-PlayStation-5-Edición-Digital-825-gb-SSD-Blanco/p/100048458?gclid=CjwKCAjwvrOpBhBdEiwAR58-3EjvtQ7Hz-2tSyPOpTSKYsBkRSPjQUYuS-h7GAjOK46K9LC-0yCbQRoCa4gQAvD_BwE')
CP = obhtml('https://www.cyberpuerta.mx/Audio-y-Video/Consolas-y-Juegos/PlayStation-5-PS5/Consolas-PlayStation-5/Sony-PlayStation-5-Digital-Edition-825GB-WiFi-Bluetooth-5-1-Blanco-Negro.html?gclid=CjwKCAjwvrOpBhBdEiwAR58-3Gdg_MRhYkfRRhFS6ZS8B9htEm3O2Ni7nhXg8spRLx0QTPsnbnNu8hoCgQ4QAvD_BwE')

precioML = MercadoLibre(ML)
precioRS = RadioShack(RS)
precioCP = Cyberpuerta(CP)

precios = {'Mercado Libre': precioML, 'Radio Shack': precioRS, 'Cyber Puerta': precioCP}
barato = min(precios, key=precios.get)
mensaje = f"El PlayStation 5 más barato se encuentra en: {barato}"

with open('C:/Users/yeyos/OneDrive/Documentos/ReportePrecios.csv', 'w', newline='') as archivo:
    csv_writer = csv.writer(archivo)
    csv_writer.writerow(['', 'Mercado Libre', 'Radio Shack', 'Cyber Puerta'])
    csv_writer.writerow(['precios', precioML, precioRS, precioCP])
    csv_writer.writerow([])
    csv_writer.writerow([mensaje])

print("Archivo CSV guardado con éxito.")

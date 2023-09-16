import pandas as pd
import folium
from shapely import wkt
from fpdf import FPDF
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

df = pd.read_csv("C:/Users/yeyos/Downloads/new-york-city-art-galleries-1.csv")

df = df.drop_duplicates()

df = df.drop(columns=['ADDRESS2'])

df = df[df['CITY'] == 'Brooklyn']

df = df.sort_values(by='GRADING', ascending=False)

jsjs = df['the_geom'].head(3).apply(wkt.loads)   #coordenadas
cord3 = [list(geom.coords)[0] for geom in jsjs]

latitud = sum([coord[1] for coord in cord3]) / 3 #centrar mapa
longitud = sum([coord[0] for coord in cord3]) / 3

jaja = folium.Map(location=[latitud, longitud], zoom_start=13)
for coord in cord3:
    folium.Marker(location=coord[::-1], icon=folium.Icon(color='red')).add_to(jaja)

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080') # guardar mapa como imagen
driver = webdriver.Chrome(options=options)

mapaHTML = "C:/Users/yeyos/OneDrive/Documentos/mapa.html"
mapaPNG = "C:/Users/yeyos/OneDrive/Documentos/mapa.png"
jaja.save(mapaHTML)

driver.get('file://' + mapaHTML)

zoom = ActionChains(driver)
zoom.key_down(Keys.CONTROL).send_keys(Keys.SUBTRACT).key_up(Keys.CONTROL).perform() #zoom al mapa 

driver.save_screenshot(mapaPNG)
driver.quit()

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=11)
pdf.cell(200, 10, txt="Los mejores museos y galerias", ln=True, align='C')
pdf.image(mapaPNG, x = 10, y = None, w = 190)

museos = df.head(3)
for indice, row in enumerate(museos.iterrows(), start=1):
    _, row = row  
    cuerpo = f"{indice}. Nombre: {row['NAME']}\nDirección: {row['ADDRESS1']}\nCalificación: {row['GRADING']}"
    pdf.ln(10)
    pdf.multi_cell(0, 10, txt=cuerpo)

hola = "C:/Users/yeyos/OneDrive/Documentos/reportemuseos.pdf"
pdf.output(hola)

df.to_csv("C:/Users/yeyos/OneDrive/Documentos/TerceraPrac.csv", index=False)






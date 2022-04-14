from bs4 import BeautifulSoup
import requests

aemet_url = 'https://www.aemet.es/es/eltiempo/prediccion/municipios/'
page = requests.get(aemet_url)

aemet_html = page.text
print(aemet_html)

soup = BeautifulSoup(aemet_html, 'html.parser')
links = []

for link in soup.find_all('a'):
    if ("/es/eltiempo/prediccion/municipios?p" in str(link.get('href'))):
        links.append(link.get('href'))


ciudades = {
    "15": "A Coruña",
    "03": "Alacant/Alicante",
    "02": "Albacete",
    "04": "Almería",
    "01": "Araba/Álava",
    "33": "Asturias",
    "05": "Ávila",
    "06": "Badajoz",
    "08": "Barcelona",
    "48": "Bizkaia",
    "09": "Burgos",
    "10": "Cáceres",
    "11": "Cádiz",
    "39": "Cantabria",
    "12": "Castelló/Castellón",
    "51": "Ceuta",
    "13": "CiudadReal",
    "14": "Córdoba",
    "16": "Cuenca",
    "17": "Girona",
    "18": "Granada",
    "19": "Guadalajara",
    "20": "Gipuzkoa",
    "21": "Huelva",
    "22": "Huesca",
    "07": "IllesBalears",
    "23": "Jaén",
    "26": "LaRioja",
    "35": "LasPalmas",
    "24": "León",
    "25": "Lleida",
    "27": "Lugo",
    "28": "Madrid",
    "29": "Málaga",
    "52": "Melilla",
    "30": "Murcia",
    "31": "Navarra",
    "32": "Ourense",
    "34": "Palencia",
    "36": "Pontevedra",
    "37": "Salamanca",
    "38": "SantaCruzdeTenerife",
    "40": "Segovia",
    "41": "Sevilla",
    "42": "Soria",
    "43": "Tarragona",
    "44": "Teruel",
    "45": "Toledo",
    "46": "València/Valencia",
    "47": "Valladolid",
    "49": "Zamora",
    "50": "Zaragoza"}

print(ciudades["10"])

print(*links, sep="\n")


#<li<a href="/es/eltiempo/prediccion/municipios?p=15"A Coruña</a</li
# soup = BeautifulSoup(html_doc, 'html.parser')
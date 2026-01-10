import requests
from bs4 import BeautifulSoup
import time
import csv

base_url = "http://books.toscrape.com/catalogue/"
url_actual = "http://books.toscrape.com/catalogue/page-1.html"
headers = {'User-Agent': 'Mozilla/5.0...'} # Tu disfraz

while url_actual:
    print(f"Rastreando: {url_actual}")
    res = requests.get(url_actual, headers=headers)
    sopa = BeautifulSoup(res.text, 'html.parser')
    
    libros = sopa.select('.product_pod')
    lista_libros = []

    for libro in libros:
        # Buscamos dentro de cada libro
        titulo = libro.select_one('h3 a')['title']
        precio = libro.select_one('.price_color')
        # De cada precio, se extrae el texto con .text
        # Con .replace('Â£', '') se "reemplazan" los simbolos que no nos sirven por nada porque en realidad se quitan
        # Ya que estamos trabajando con valores y puede que necesitemos hacer operaciones matemáticas se transforman los precios a float
        precio_final = float(precio.text.replace('Â£', ''))
        
        # Guardamos los datos en un formato estructurado
        lista_libros.append({
            'Titulo': titulo,
            'Precio': precio_final
        })

        # Se guarda la información en un archivo CSV
    with open('mis_libros.csv', 'w', newline='', encoding= 'utf-8') as archivo:
        # Definimos los nombres de las columnas
        columnas = ['Titulo', 'Precio']
        escritor = csv.DictWriter(archivo, fieldnames= columnas)

        escritor.writeheader() # Escribe los nombres en la primera fila
        escritor.writerows(lista_libros)
    
    # BUSCAMOS EL BOTÓN SIGUIENTE
    # En este sitio, el botón está en un <li> con clase 'next'
    boton_siguiente = sopa.select_one('li.next a')
    
    if boton_siguiente:
        # Construimos la nueva URL (concatenando la base + el href del botón)
        url_actual = base_url + boton_siguiente['href']
        time.sleep(2) # Pausa de cortesía
    else:
        print("¡Hemos llegado a la última página!")
        url_actual = None # Esto rompe el bucle while
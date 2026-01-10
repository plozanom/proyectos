import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com"
respuesta = requests.get(url)

if respuesta.status_code == 200:
    # Aquí es donde ocurre la magia
    sopa = BeautifulSoup(respuesta.text, 'html.parser')
    
    # Buscamos la etiqueta del título principal
    titulo = sopa.find('a').text
    if titulo:
        print(f"El texto encontrado es: {titulo}")
    else:
        print("No se encontró el titulo")
    
    # Suponiendo que ya tenemos nuestra 'sopa' lista
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
        
    print("El archivo CSV ha sido creado con exito")
else:
    print(f"Error al acceder: {respuesta.status_code}")
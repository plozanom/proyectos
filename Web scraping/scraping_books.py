import requests
from bs4 import BeautifulSoup

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

    for libro in libros:
        # Buscamos dentro de cada libro
        titulo = libro.select_one('h3 a')['title']
        precio = libro.select_one('.price_color')
        # De cada precio, se extrae el texto con .text
        # Con .replace('Â£', '') se "reemplazan" los simbolos que no nos sirven por nada porque en realidad se quitan
        # Ya que estamos trabajando con valores y puede que necesitemos hacer operaciones matemáticas se transforman los precios a float
        precio_final = float(precio.text.replace('Â£', ''))
        print(f"Libro: {titulo} | Precio: {precio_final}")
else:
    print(f"Error al acceder: {respuesta.status_code}")
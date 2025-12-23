# Función que genera un html básico

def generador_html():
    esqueleto = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Aquí va un titulo</title>
    </head>
    <body>
        <h1>¡Hola desde Python!</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        Nunc libero sem, convallis ut neque in, placerat ornare diam. 
        Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Maecenas porttitor et felis sit amet faucibus. 
        Proin odio velit, aliquam at pulvinar quis, hendrerit nec metus. 
        Sed a tortor vehicula, laoreet lectus vel, dapibus massa.</p>
    </body>
    </html>
    """

    with open("main.html", "w") as file:
        file.write(esqueleto)
    
    return "Esqueleto de pagina web creada"

print(generador_html())
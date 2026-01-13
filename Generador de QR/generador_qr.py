# Función para crear qr
# Nota: Se necesita de la librería pillow aunque no la utilices directamente

import qrcode

def generador_qr(link, archivo):
    qr = qrcode.QRCode(box_size= 20, border= 5)
    qr.add_data(link)

    imagen = qr.make_image(fill_color= "black", back_color= "white")
    imagen.save(archivo)

    return "QR creado con exito"

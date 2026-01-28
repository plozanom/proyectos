import smtplib


def enviar_email(destino, contenido, smtp_server, direccion_envio, password):
    try:
        server = smtplib.SMTP(smtp_server, 587)
        server.ehlo()
        server.starttls()
        server.login(direccion_envio, password)
        server.sendmail(direccion_envio, destino, contenido)
        server.close()
    except Exception as e:  # Muestra cualquier error
        print(e)

# Esta función recibe una entrada de diario y retorna un archivo txt de nombre 'diario' con todas las entradas con su fecha de escritura
from datetime import date
def diario(contenido):

    with open("diario.txt", 'a') as d:
        d.write(date.today().strftime("%A %b %d %Y"))
        d.write("\n")
        d.write(f"{contenido}\n\n")

contenido = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce lacus libero, consectetur nec augue vehicula, venenatis aliquam nisi. Nulla facilisi. Praesent tempor nibh tincidunt nibh luctus, eu fringilla lorem aliquet. Vestibulum gravida sollicitudin libero eget molestie. Maecenas vitae lacus ac lectus luctus laoreet sit amet in dui. Donec vitae sem tortor. Duis ut urna ac quam faucibus accumsan. Aenean eu pellentesque massa, et iaculis felis. Mauris sit amet est lacus. Nullam pulvinar elementum rutrum. Cras sit amet aliquet tellus, et varius sem."

diario(contenido)
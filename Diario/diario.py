# Esta función recibe una entrada de diario y retorna un archivo txt de nombre 'diario' con todas las entradas con su fecha de escritura
from datetime import date
def diario(contenido):

    with open("diario.txt", 'a') as d:
        d.write(date.today().strftime("%A %b %d %Y"))
        d.write("\n")
        d.write(f"{contenido}\n\n")
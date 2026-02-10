import sqlite3

# Conectando la base de datos, se creará la base de datos 'primer_intento', si ya existe solo hace la conexión
conexion = sqlite3.connect("biblioteca.db")

# Se crea un objeto 'cursor' que es el que ejecuta las instrucciones SQL
cursor = conexion.cursor()

# Se hace la consulta
cursor.execute("SELECT * FROM libros")

# Se obtienen los resultados
# Nota: Existen 3 formas de obtener los resultados:
#   fetchone() - Solo trae la primera fila (Para busqueda de datos unicos)
#   fetchall() - Que trae todos los datos como una lista de tuplas
#   fetchmany(n) - Que trae n numero de filas
libros = cursor.fetchall()

# Se recorre la lista de resultados y se le da formato
for libro in libros:
    print(f"El libro {libro[1]} fue escrito por {libro[2]} en el año {libro[3]}")

# Cuando la consulta es extensa, buscar por posición en la tupla es engorroso
# Se puede utilizar Row Factory que es configurar la conexión para que devuelva algo parecido a un diccionario en vez de una tupla, ej:
conexion.row_factory = sqlite3.Row
cursor2 = conexion.cursor()

cursor2.execute("SELECT * FROM libros")
libros2 = cursor2.fetchall()

for libro in libros2:
    print(
        f"El libro {libro['titulo']} fue escrito por {libro['autor']} en el año {libro['año']}"
    )

# Siempre se debe cerrar la conexión cuando se termine de usar la base de datos
conexion.close()

import sqlite3

# Establecemos la conexión y creamos la base de datos 'biblioteca'
conexion = sqlite3.connect("biblioteca.db")

# Creamos un cursor
cursor = conexion.cursor()

# Creamos una tabla llamada 'estudiantes'
# Se definen las columnas: id (numero), nombre (texto), edad (numero)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS libros (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    autor TEXT,
    año INTEGER
    )""")

# La siguiente linea guarda los cambios
conexion.commit()

print("Tabla creada con exito!!!")

# Cerramos la conexión
conexion.close()

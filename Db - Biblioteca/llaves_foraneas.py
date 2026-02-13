import sqlite3

conexion = sqlite3.connect("biblioteca_avanzada.db")
cursor = conexion.cursor()

# Se habilita el soporte de llaves foraneas (En SQLite3 viene desactivado por defecto)
cursor.execute("PRAGMA foreign_keys = ON")

# Se crea la tabla 'autores'
cursor.execute("""
    CREATE TABLE IF NOT EXISTS autores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
    )""")

# Se crea la tabla 'libros' y se relaciona con la tabla 'autores'
cursor.execute("""
    CREATE TABLE IF NOT EXISTS libros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor_id INTEGER,
    FOREIGN KEY (autor_id) REFERENCES autores (id)
    )""")

# La siguiente linea guarda los cambios
conexion.commit()

print("Tabla creada con exito!!!")

# Cerramos la conexión
conexion.close()

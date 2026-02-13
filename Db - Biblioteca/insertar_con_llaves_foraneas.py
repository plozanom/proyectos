import sqlite3

conexion = sqlite3.connect("biblioteca_avanzada.db")
cursor = conexion.cursor()

# Habilitando las llaves foraneas
cursor.execute("PRAGMA foreign_keys = ON")

# Insertando un autor en la tabla padre (autores)
cursor.execute("INSERT INTO autores (nombre) VALUES (?)", ("Gabriel García Márquez",))

# Recuperando el ultimo ID creado
id_autor = cursor.lastrowid

# Insertando varios de los titulos del autor en la tabla hija (obras)
lista_libros = [
    ("Cien años de soledad", id_autor),
    ("El amor en los tiempos del cólera", id_autor),
]

cursor.executemany(
    "INSERT INTO libros (titulo, autor_id) VALUES ( ?, ?)",
    lista_libros,
)

# Guardando los cambios
conexion.commit()

print("Inserción de datos exitosa!!!")
# Cerrando la conexión
conexion.close()

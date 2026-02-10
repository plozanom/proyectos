import sqlite3

# Conectando la base de datos, se creará la base de datos 'primer_intento', si ya existe solo hace la conexión
conexion = sqlite3.connect("biblioteca.db")

# Se crea un objeto 'cursor' que es el que ejecuta las instrucciones SQL
cursor = conexion.cursor()

# Se borra un libro especifico por su ID
cursor.execute("DELETE FROM libros WHERE id = ?", (20,))
conexion.commit()

print(f"Se borraron {cursor.rowcount} entradas")
# Siempre se debe cerrar la conexión cuando se termine de usar la base de datos
conexion.close()

import sqlite3

conexion = sqlite3.connect("biblioteca_avanzada.db")
conexion.row_factory = sqlite3.Row  # Se usa para usar nombres de las columnas, ej: libros.autor_id

cursor = conexion.cursor()

# Escribiendo la consulta como una variable
consulta = """
SELECT libros.titulo, autores.nombre
FROM libros
INNER JOIN autores ON libros.autor_id = autores.id
ORDER BY autores.nombre ASC, obras.titulo ASC"""

cursor.execute(consulta)
filas = cursor.fetchall()

for fila in filas:
    print(f"Libro: {fila['titulo']} | Autor: {fila['nombre']}")

conexion.close()

import sqlite3

conexion = sqlite3.connect("mi_prueba.db")
conexion.row_factory = sqlite3.Row

cursor = conexion.cursor()

# Escribiendo la consulta como una variable
consulta = """
SELECT autores.nombre, obras.titulo
FROM autores
LEFT JOIN obras ON autores.id = obras.autor_id"""

cursor.execute(consulta)
filas = cursor.fetchall()

for fila in filas:
    print(f"Autor: {fila['nombre']} | Libro: {fila['titulo']}")

conexion.close()

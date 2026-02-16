import sqlite3
from contextlib import closing

database = "mi_prueba.db"

try:
    with closing(sqlite3.connect(database)) as conexion:
        # Importante: activar PRAGMA dentro de la conexión
        conexion.execute("PRAGMA foreign_keys = ON")

        with conexion:  # Inicia transacción
            conexion.row_factory = sqlite3.Row
            cursor = conexion.cursor()

            consulta = """
            SELECT autores.nombre, COUNT(obras.id) as total_libros
            FROM autores
            LEFT JOIN obras ON autores.id = obras.autor_id
            GROUP BY autores.id"""

            cursor.execute(consulta)

            filas = cursor.fetchall()
            for fila in filas:
                print(f"Autor: {fila['nombre']} | Total: {fila['total_libros']} ")


except sqlite3.Error as e:
    print(f"Error general de SQLite: {e}")

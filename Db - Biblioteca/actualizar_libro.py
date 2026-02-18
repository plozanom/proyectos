import sqlite3
from contextlib import closing

database = "biblioteca.db"

try:
    with closing(sqlite3.connect(database)) as conexion:
        with conexion:
            cursor = conexion.cursor()

            # Se cambiará el titulo del libro con ID 4
            nuevo_titulo = "Don Quijote de la Mancha (Edición Revisada)"
            id_buscado = 4

            # Actualización del nombre del libro
            # Nota: Siempre poner un WHERE en la consulta o sino todos los datos en la tabla se actualizarán
            cursor.execute(
                """
                UPDATE libros
                SET titulo = ?
                WHERE id = ?""",
                (nuevo_titulo, id_buscado),
            )

            print(
                f"Filas actualizadas: {cursor.rowcount}"
            )  # rowcount cuenta cuantas filas han sido afectadas por la instrucción dada

except sqlite3.Error as e:
    print(f"Error general de SQLite: {e}")

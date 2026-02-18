import sqlite3
from contextlib import closing

database = "biblioteca_avanzada.db"

try:
    with closing(sqlite3.connect(database)) as conexion:
        # Importante: activar PRAGMA dentro de la conexión
        conexion.execute("PRAGMA foreign_keys = ON")

        with conexion:  # Inicia transacción
            cursor = conexion.cursor()
            # Intentamos borrar un autor que tiene libros
            cursor.execute("DELETE FROM autores WHERE id = 1")

# El error ocurre cuando se intenta borrar algo que daña la integridad de la base de datos, en este caso, un autor que tiene vinculados libros
except sqlite3.IntegrityError as e:
    print(
        f"Error de integridad: No se puede borrar porque tiene libros asociados. Detalle: {e}"
    )
except sqlite3.Error as e:
    print(f"Error general de SQLite: {e}")

import sqlite3
from contextlib import closing
from functools import wraps
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "databases" / "gestion_proyectos.db"


def estandar_db(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        database = DATABASE_PATH
        database.parent.mkdir(parents=True, exist_ok=True)

        # Se usa el with closing dentro del decorador para estandarizar la conexión
        try:
            with closing(sqlite3.connect(database)) as conexion:
                conexion.row_factory = sqlite3.Row
                conexion.execute("PRAGMA foreign_keys = ON")

                # Se pasa la conexión a la función para que esta haga la transacción
                return func(conexion, *args, **kwargs)
        except sqlite3.Error as e:
            print(f"\nError en la base de datos: {e}")
        except Exception as e:
            print(f"\nError inesperado: {e}")

    return wrapper

from inicializadores.conexion import estandar_db


@estandar_db
def inicializar_db(conexion):
    with conexion:
        conexion.execute("PRAGMA foreign_keys = ON")

        # Tabla de Proyectos
        conexion.execute("""
                        CREATE TABLE IF NOT EXISTS proyectos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL UNIQUE
                        )""")

        # Tabla de tareas con validación de fecha
        conexion.execute("""
                        CREATE TABLE IF NOT EXISTS tareas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        proyecto_id INTEGER,
                        descripcion TEXT NOT NULL,
                        fecha_limite TEXT NOT NULL,
                        estado INTEGER DEFAULT 0,
                        FOREIGN KEY (proyecto_id) REFERENCES proyectos(id) ON DELETE CASCADE,
                        CHECK (estado IN (0, 1)),
                        CHECK (length(fecha_limite) <= 10)
                        )""")

    print("Creación/Verificación de la base de datos se ha hecho con exito")

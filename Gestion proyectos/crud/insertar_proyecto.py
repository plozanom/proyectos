from inicializadores.conexion import estandar_db


@estandar_db
def insertar_proyecto(conexion, nombre_proyecto):
    with conexion:
        cursor = conexion.cursor()

        # Insertando el proyecto
        cursor.execute("INSERT INTO proyectos (nombre) VALUES (?)", (nombre_proyecto,))

        # Recuperando el id del proyecto
        proyecto_id = cursor.lastrowid

        return proyecto_id

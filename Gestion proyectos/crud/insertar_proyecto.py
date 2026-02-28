from inicializadores.conexion import estandar_db


@estandar_db
def insertar_proyecto(conexion, nombre_proyecto):
    with conexion:
        cursor = conexion.cursor()

        # Insertando el proyecto
        cursor.execute("INSERT INTO proyectos (nombre) VALUES (?)", (nombre_proyecto,))

        return cursor.rowcount > 0


@estandar_db
def insertar_proyectos_en_masa(conexion, lista_nombres):
    with conexion:
        cursor = conexion.cursor()

        consulta = "INSERT OR IGNORE INTO proyectos (nombre) VALUES (?)"
        nombres_tuplas = [(n,) for n in lista_nombres]

        cursor.executemany(consulta, nombres_tuplas)

        return cursor.rowcount > 0

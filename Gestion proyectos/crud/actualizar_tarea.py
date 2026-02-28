from inicializadores.conexion import estandar_db


@estandar_db
def marcar_tarea_completada(conexion, tarea_id, nuevo_estado):
    with conexion:
        cursor = conexion.cursor()

        consulta = "UPDATE tareas SET estado = ? WHERE id = ?"

        cursor.execute(consulta, (nuevo_estado, tarea_id))

        return cursor.rowcount > 0


@estandar_db
def posponer_fechas_proyecto(conexion, proyecto_id, dias):
    with conexion:
        cursor = conexion.cursor()

        consulta = """UPDATE tareas SET fecha_limite = date(fecha_limite, ?)
        WHERE proyecto_id = ? AND estado = 0"""

        modificador = f"{'+' if dias >= 0 else ''}{dias} days"

        cursor.execute(consulta, (modificador, proyecto_id))

        return cursor.rowcount > 0


@estandar_db
def renombrar_proyecto(conexion, id_proyecto, nuevo_nombre):
    with conexion:
        cursor = conexion.cursor()

        consulta = "UPDATE proyectos SET nombre = ? WHERE id = ?"

        cursor.execute(consulta, (nuevo_nombre, id_proyecto))

        return cursor.rowcount > 0


@estandar_db
def actualizar_tarea_manera_segura(
    conexion, tarea_id, nueva_desc=None, nueva_fecha=None
):
    with conexion:
        cursor = conexion.cursor()

        consulta = """
        UPDATE tareas
        SET descripcion = COALESCE(?, descripcion)
            fecha_limite = COALESCE(?, fecha_limite)
        WHERE id = ? AND estado = 0"""

        cursor.execute(consulta, (nueva_desc, nueva_fecha, tarea_id))

        return cursor.rowcount > 0

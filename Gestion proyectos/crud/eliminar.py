from inicializadores.conexion import estandar_db


@estandar_db
def eliminar_proyecto(conexion, proyecto_id):
    with conexion:
        cursor = conexion.cursor()

        consulta = "DELETE FROM proyectos WHERE id = ?"

        cursor.execute(consulta, (proyecto_id,))

        if cursor.rowcount > 0:
            print(f"Proyecto {proyecto_id} y sus tareas han sido eliminados.")
        else:
            print(f"No se encontró el proyecto con ID {proyecto_id}.")


@estandar_db
def limpiar_tareas_antiguas(conexion, dias_antiguedad=30):
    with conexion:
        cursor = conexion.cursor()

        consulta = """
        DELETE FROM tareas
        WHERE estado = 1
        AND date(fecha_limite) < date('now', ?)"""

        modificador = f"-{dias_antiguedad} days"

        cursor.execute(consulta, (modificador,))

        if cursor.rowcount > 0:
            print(f"Se hizo la limpieza de {cursor.rowcount} tareas antiguas.")
        else:
            print(
                f"No se encontraron tareas con más de {dias_antiguedad} dias de antiguedad."
            )

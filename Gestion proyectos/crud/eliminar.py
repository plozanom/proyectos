from inicializadores.conexion import estandar_db


@estandar_db
def limpiar_proyectos_huerfanos(conexion):
    with conexion:
        cursor = conexion.cursor()

        consulta = """
        DELETE FROM proyectos
        WHERE id NOT IN (SELECT DISTINCT proyecto_id FROM tareas)"""

        cursor.execute(consulta)

        return cursor.rowcount > 0


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

        return cursor.rowcount > 0

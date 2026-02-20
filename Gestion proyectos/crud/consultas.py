from inicializadores.conexion import estandar_db


@estandar_db
def obtener_tareas_por_fecha(conexion, fecha):
    with conexion:
        cursor = conexion.cursor()

        consulta = """
        SELECT t.descripcion, p.nombre as proyecto
        FROM tareas t
        JOIN proyectos p ON t.proyecto_id = p.id
        WHERE date(t.fecha_limite) = date(?)
        ORDER BY t.descripcion ASC"""

        cursor.execute(
            consulta,
            fecha,
        )

        return cursor.fetchall()

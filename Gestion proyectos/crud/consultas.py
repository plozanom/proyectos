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


@estandar_db
def obtener_tareas_proximas(conexion, dias):
    with conexion:
        cursor = conexion.cursor()

        consulta = """
        SELECT t.descripcion, t.fecha_limite, p.nombre as proyecto
        FROM tareas t
        JOIN proyectos p ON t.proyecto_id = p.id
        WHERE date(t.fecha_limite) <= date('now', ?)
        ORDER BY t.fecha_limite ASC"""

        cursor.execute(consulta, f"+{dias} days")

        return cursor.fetchall()


@estandar_db
def obtener_tareas_criticas(conexion):
    with conexion:
        cursor = conexion.cursor()

        consulta = """
        SELECT t.descripcion, t.fecha_limite, p.nombre as proyecto
        FROM tareas t
        JOIN proyectos p ON t.proyecto_id = p.id
        WHERE t.estado = 0 AND date(t.fecha_limite) < date('now')
        ORDER BY t.fecha_limite DESC"""

        cursor.execute(consulta)

        return cursor.fetchall()


@estandar_db
def obtener_todas_las_tareas(conexion):
    with conexion:
        cursor = conexion.cursor()

        consulta = """
        SELECT t.descripcion, t.fecha_limite, p.nombre as proyecto
        FROM tareas t
        JOIN proyectos p ON t.proyecto_id = p.id
        ORDER BY p.nombre ASC t.fecha_limite ASC"""

        cursor.execute(consulta)

        return cursor.fetchall()


@estandar_db
def obtener_tareas_de_proyecto(conexion, nombre_proyecto):
    with conexion:
        cursor = conexion.cursor()

        consulta = """
        SELECT t.descripcion, t.fecha_limite, p.nombre as proyecto
        FROM tareas t
        JOIN proyectos p ON t.proyecto_id = p.id
        WHERE p.nombre = ?
        ORDER BY t.fecha_limite ASC"""

        cursor.execute(consulta, (nombre_proyecto,))

        return cursor.fetchall()

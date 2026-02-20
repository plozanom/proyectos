from inicializadores.conexion import estandar_db


@estandar_db
def insertar_tarea(conexion, proyecto_id, descripcion, fecha):
    with conexion:
        cursor = conexion.cursor()

        # Insertando una tarea a un proyecto existente
        cursor.execute(
            """
            INSERT INTO tareas (proyecto_id, descripcion, fecha_limite)
            VALUES (?, ?, ?,)""",
            (proyecto_id, descripcion, fecha),
        )

        print("Tarea registrada")


@estandar_db
def insertar_grupo_tareas(conexion, proyecto_id, descripcion_y_fecha):
    """
    Esta función recibe la conexión del decorador (como las otras funciones), un ID del proyecto (que viene de la función insertar_proyecto) y
    una lista de tuplas con la descripción y la fecha_limite [(desc, fecha), ...]
    """

    lista_valores = [(proyecto_id, *tarea) for tarea in descripcion_y_fecha]

    consulta = (
        "INSERT INTO tareas (proyecto_id, descripcion, fecha_limite) VALUES (?, ?, ?)"
    )

    with conexion:
        cursor = conexion.cursor()

        cursor.executemany(consulta, lista_valores)

    print(f"Se ha hecho el registro de {len(lista_valores)} tareas de manera exitosa")

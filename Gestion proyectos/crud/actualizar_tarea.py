from inicializadores.conexion import estandar_db


@estandar_db
def marcar_tarea_completada(conexion, tarea_id, nuevo_estado):
    with conexion:
        cursor = conexion.cursor()

        consulta = "UPDATE tareas SET estado = ? WHERE id = ?"

        cursor.execute(consulta, (nuevo_estado, tarea_id))

        # Verificamos si realmente se actualizó algo
        if cursor.rowcount > 0:
            print(f"Tarea con ID {tarea_id} marcada como completada.")
        else:
            print(f"No se encontró ninguna tarea con el ID {tarea_id}.")


@estandar_db
def posponer_fechas_proyecto(conexion, proyecto_id, dias):
    with conexion:
        cursor = conexion.cursor()

        consulta = """UPDATE tareas SET fecha_limite = date(fecha_limite, ?)
        WHERE proyecto_id = ? AND estado = 0"""

        modificador = f"{'+' if dias >= 0 else ''}{dias} days"

        cursor.execute(consulta, (modificador, proyecto_id))

        if cursor.rowcount > 0:
            print(
                f"Se han pospuesto {cursor.rowcount} tareas del proyecto {proyecto_id} en {dias} dias."
            )
        else:
            print(f"No hay tareas pendientes para posponer del proyecto {proyecto_id}.")

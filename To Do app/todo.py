# Funciones para la gestión de una app de tareas.
# La función 'archivo' crea (si no existe) un archivo json que funcionará como base de datos. Recibe la ruta del archivo en la que se creará la base de datos.
# La función 'cargar_tareas', como su nombre lo indica, carga en memoria todo lo que se encuentre en el archivo json. Recibe la ruta del archivo.
# La función 'guardar_tareas' guarda los cambios hechos en el archivo json. Recibe la ruta del archivo y las tareas, tanto las que se encuentran en memoria gracias a 'cargar_tareas' como las nuevas creadas con 'nueva_tarea'.
# La función 'nueva_tarea' crea una nueva tarea. Recibe la ruta del archivo y la especificación de la nueva tarea.
# La función 'ver_tareas' nos deja ver las tareas y su estado. Recibe la ruta del archivo json.
# La función 'actualizar_estado' actualiza el estado de una tarea de "Sin terminar" a "Terminada". Recibe la ruta del archivo y el id de la tarea a actualizar.
# La función 'borrar_tarea' borra una tarea especificada y cambia la numeración de las tareas restantes. Recibe la ruta del archivo y el id de la tarea a borrar.

import json
from os import path


def archivo(base_de_datos):
    if not path.exists(base_de_datos):
        with open(base_de_datos, "w") as db:
            json.dump([], db)


def cargar_tareas(base_de_datos):
    with open(base_de_datos, "r") as db:
        return json.load(db)


def guardar_tareas(base_de_datos, tareas):
    with open(base_de_datos, "w") as db:
        json.dump(tareas, db, indent=2)


def nueva_tarea(base_de_datos, tarea):
    tareas = cargar_tareas(base_de_datos)
    id = len(tareas) + 1
    tareas.append({"ID": id, "Tarea": tarea, "Estado": "Sin terminar"})
    guardar_tareas(base_de_datos, tareas)
    print("Tarea agregada")


def ver_tareas(base_de_datos):
    tareas = cargar_tareas(base_de_datos)
    if tareas:
        for tarea in tareas:
            print(f"{tarea['ID']}. {tarea['Tarea']} - Estado: {tarea['Estado']}")
    else:
        print("No se han encontrado tareas")


def actualizar_estado(base_de_datos, id_tarea):
    tareas = cargar_tareas(base_de_datos)
    existe_id = False
    for tarea in tareas:
        if tarea["ID"] == id_tarea:
            tarea["Estado"] = "Terminada"
            existe_id = True

    if existe_id:
        guardar_tareas(base_de_datos, tareas)
    else:
        print("ID no encontrado")


def borrar_tarea(base_de_datos, id_tarea):
    tareas = cargar_tareas(base_de_datos)
    tareas_actualizadas = [tarea for tarea in tareas if tarea["ID"] != id_tarea]
    for num, tarea in enumerate(tareas_actualizadas):
        tarea["ID"] = num + 1

    if len(tareas) > len(tareas_actualizadas):
        guardar_tareas(base_de_datos, tareas_actualizadas)
    else:
        print("ID no encontrado")

from crud.insertar_proyecto import insertar_proyecto
from crud.insertar_tarea import insertar_grupo_tareas_por_nombre_proyecto
from inicializadores.inicializador import inicializar_db


# Advertencia: Si usas basedpyright, el idiota no reconocerá el decorador, por lo que marcará las funciones en rojo porque no 've' la conexión con sqlite
def main():
    inicializar_db()

    # Definición de la estructura de datos para la carga
    # Usamos un diccionario para mantener la relación Proyecto -> Lista de Tareas
    datos_carga = {
        "Reforma Cocina": [
            ("Comprar azulejos", "2026-03-10"),
            ("Demoler pared antigua", "2026-03-12"),
            ("Instalar fontanería", "2026-03-15"),
        ],
        "App Inventario": [
            ("Diseñar base de datos", "2026-03-05"),
            ("Configurar servidor API", "2026-03-08"),
        ],
        "Mantenimiento Jardín": [
            ("Podar árboles", "2026-04-01"),
            ("Instalar riego automático", "2026-04-05"),
        ],
    }

    print("--- 🚀 Iniciando Carga Masiva de Datos ---")

    for nombre_proyecto, tareas in datos_carga.items():
        # Intentamos crear el proyecto
        if insertar_proyecto(nombre_proyecto):
            print(f"\n📁 Proyecto '{nombre_proyecto}' creado.")
        else:
            print(
                f"\n📁 El proyecto '{nombre_proyecto}' ya existía (se omitió creación)."
            )

        # Insertamos su grupo de tareas usando el subquery por nombre
        if insertar_grupo_tareas_por_nombre_proyecto(nombre_proyecto, tareas):
            print(f"  ✅ {len(tareas)} tareas asignadas correctamente.")
        else:
            print(f"  ❌ No se pudieron asignar tareas a '{nombre_proyecto}'.")

    print("\n--- ✨ Proceso finalizado ---")


if __name__ == "__main__":
    main()

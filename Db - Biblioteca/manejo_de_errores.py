import sqlite3

try:
    conexion = sqlite3.connect("biblioteca.db")
    cursor = conexion.cursor()

    # Probar con una tabla inexistente
    cursor.execute("SELECT * FROM usuarios")

except sqlite3.Error as e:
    print(f"¡Oops! Ocurrió un error de base de datos: {e}")

finally:
    if conexion:
        conexion.close()
        print("Conexión cerrada")

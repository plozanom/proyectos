import sqlite3

conexion = sqlite3.connect("biblioteca.db")
cursor = conexion.cursor()

# Insertando una sola fila de datos
titulo_libro = "Cien años de soledad"
autor_libro = "Gabriel García Márquez"
primera_publicacion = 1967

cursor.execute(
    """
    INSERT INTO libros (titulo, autor, año)
    VALUES (?, ?, ?)""",
    (titulo_libro, autor_libro, primera_publicacion),
)

# Insertando más de una fila de datos
lista_libros = [
    ("1984", "George Orwell", 1949),
    ("La sombra del viento", "Carlos Ruiz Zafón", 2001),
]

# Se usan placeholders ('?') como espacios reservados
# Nota: NUNCA se deben usar f-strings ni concatenaciones para insertar datos para evitar ataques de inyección SQL
# Se usa executemany en vez de execute
cursor.executemany(
    """
    INSERT INTO libros (titulo, autor, año)
    VALUES (?, ?, ?)""",
    lista_libros,
)

# Siempre usar commit para guardar los cambios
conexion.commit()

print("Datos insertados con exito!!!!")

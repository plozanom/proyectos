import sqlite3

conexion = sqlite3.connect("biblioteca.db")
cursor = conexion.cursor()

# Insertando más de una fila de datos
lista_libros = [
    ("Don Quijote de la Mancha", "Miguel de Cervantes", 1605),
    ("Hamlet", "William Shakespeare", 1603),
    ("Orgullo y prejuicio", "Jane Austen", 1813),
    ("Crónica de una muerte anunciada", "Gabriel García Márquez", 1981),
    ("Fahrenheit 451", "Ray Bradbury", 1953),
    ("El principito", "Antoine de Saint-Exupéry", 1943),
    ("Guerra y paz", "Lev Tolstói", 1869),
    ("Moby Dick", "Herman Melville", 1851),
    ("La Odisea", "Homero", -800),  # Siglo VIII a.C.
    ("Crimen y castigo", "Fiódor Dostoyevski", 1866),
    ("El viejo y el mar", "Ernest Hemingway", 1952),
    ("Ensayo sobre la ceguera", "José Saramago", 1995),
    ("Rayuela", "Julio Cortázar", 1963),
    ("La metamorfosis", "Franz Kafka", 1915),
    ("Pedro Páramo", "Juan Rulfo", 1955),
    ("Código Limpio (Clean Code)", "Robert C. Martin", 2008),
    ("Fluent Python", "Luciano Ramalho", 2015),
    ("Python para todos", "Charles Severance", 2016),
    ("El alquimista", "Paulo Coelho", 1988),
    ("Frankenstein", "Mary Shelley", 1818),
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

conexion.close()

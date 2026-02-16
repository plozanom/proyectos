import sqlite3

# El Context Manager es utilizar 'with' para que gestione la conexión, el posible commit o rollback de manera segura
with sqlite3.connect("biblioteca_avanzada.db") as conexion:
    cursor = conexion.cursor()

    # Habilitando las llaves foraneas
    cursor.execute("PRAGMA foreign_keys = ON")

    # Insertando un autor en la tabla padre (autores)
    autor = "Agatha Christie"
    cursor.execute("INSERT INTO autores (nombre) VALUES (?)", (autor,))

    # Recuperando el ultimo ID creado
    id_autor = cursor.lastrowid

    # Insertando varios de los titulos del autor en la tabla hija (obras)
    lista_libros = [
        ("El asesinato de Roger Ackroyd", id_autor),
        ("Asesinato en el Orient Express", id_autor),
        ("Diez negritos", id_autor),
    ]

    cursor.executemany(
        "INSERT INTO obras (titulo, autor_id) VALUES ( ?, ?)",
        lista_libros,
    )

    print(f"Inserción del autor {autor} y de sus titulos fue exitosa")

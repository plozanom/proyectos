import tkinter as tk

# Ventana principal
root = tk.Tk()
root.title("Aplicacion Simple")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Etiqueta del titulo
title_label = tk.Label(
    root, text="Esta es mi primera app con tkinter", font=("Arial", 18), bg="#f0f0f0"
)
title_label.pack(pady=20)

# Etiqueta de peticion
name_label = tk.Label(root, text="Ingrese su nombre:", font=("Arial", 12), bg="#f0f0f0")
name_label.pack()

# Creación de una entrada (metodo entry)
entrada = tk.Entry(root, font=("Arial", 12), width=30)
entrada.pack(pady=10)


# Funcion saludo()
def saludo_usuario():
    nombre = entrada.get()

    if nombre:
        etiqueta_saludo.config(text=f"Hola, {nombre}!", fg="green")
    else:
        etiqueta_saludo.config(text="Por favor, introce tu nombre", fg="red")


# Funcion reinicio()
def reinicio():
    entrada.delete(0, tk.END)
    etiqueta_saludo.config(text="")


# Boton saludo
btn_saludo = tk.Button(
    root,
    text="Saludame",
    command=saludo_usuario,
    font=("Arial", 12),
    bg="#4caf50",
    fg="white",
)
btn_saludo.pack(pady=10)

# Boton reinicio
btn_reinicio = tk.Button(
    root,
    text="Reinicio",
    command=reinicio,
    font=("Arial", 12),
    bg="#f44336",
    fg="white",
)
btn_reinicio.pack(pady=5)

# Etiqueta de saludo
etiqueta_saludo = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0")
etiqueta_saludo.pack(pady=20)

# Correr la aplicacion
root.mainloop()

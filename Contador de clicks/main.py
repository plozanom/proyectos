import tkinter as tk

root = tk.Tk()
root.title("Contador de Clicks")
root.geometry("400x300")
root.configure(bg="#e3f2fd")

# Contador
contador = 0


# funcion de incremento
def incremento():
    global contador
    contador += 1
    etq_contador.config(text=f"Clicks: {contador}")


# Funcion de reinicio
def reinicio():
    global contador
    contador = 0
    etq_contador.config(text="Clicks: 0")


# Etiqueta de titulo
etq_titulo = tk.Label(root, text="Contador de Clicks", font=("Arial", 20), bg="#e3f2fd")
etq_titulo.pack(pady=20)

# Etiqueta del contador
etq_contador = tk.Label(root, text="Clicks: 0", font=("Arial", 16), bg="#e3f2fd")
etq_contador.pack(pady=10)

# Boton de incremento
btn_incremento = tk.Button(
    root,
    text="Click me",
    command=incremento,
    font=("Arial", 14),
    bg="#4caf50",
    fg="white",
)
btn_incremento.pack(pady=10)

# Boton de reinicio
btn_reinicio = tk.Button(
    root,
    text="Reinicio",
    command=reinicio,
    font=("Arial", 14),
    bg="#f44336",
    fg="white",
)
btn_reinicio.pack(pady=10)

# Boton de salida (Solo es por practica, si lo piensas, es bastante inutil teniendo un boton de cerrar)
btn_salida = tk.Button(
    root,
    text="Salida",
    command=root.destroy,
    font=("Arial", 14),
    bg="#607d8b",
    fg="white",
)
btn_salida.pack(pady=20)

# Correr la app
root.mainloop()

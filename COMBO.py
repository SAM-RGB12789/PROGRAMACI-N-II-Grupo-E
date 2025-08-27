import tkinter as tk
from tkinter import ttk  # Importa ttk explícitamente para evitar advertencias
from tkinter import messagebox

# CREAR VENTANA PRINCIPAL
ventana = tk.Tk()  # Instancia correctamente la ventana
ventana.title("Ejemplo Combobox")
ventana.geometry("300x200")

# Etiqueta
etiqueta = tk.Label(ventana, text="Seleccione especialidad: ")
etiqueta.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Crear combobox
opciones = ["Cardiología", "Neurología", "Pediatría", "Dermatología"]  # Corrige ortografía
combo = ttk.Combobox(ventana, values=opciones, state="readonly")
combo.current(0)  # Seleccionar primera opción por defecto
combo.grid(row=0, column=1, padx=10, pady=10)

# Función para mostrar la selección
def mostrar():
    seleccion = combo.get()
    messagebox.showinfo("Selección", f"Has elegido: {seleccion}")

# Botón para confirmar selección
boton = tk.Button(ventana, text="Aceptar", command=mostrar)
boton.grid(row=1, column=0, columnspan=2, pady=15)

ventana.mainloop()

####repair github
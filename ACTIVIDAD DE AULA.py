
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def guardar_datos():
	nombre = entry_nombre.get().strip()
	especialidad = combo_especialidad.get().strip()
	anios = entry_anios.get().strip()
	sexo = var_sexo.get()
	hospital = combo_hospital.get().strip()
	if not (nombre and especialidad and anios and sexo and hospital):
		messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos.")
		return
	try:
		anios_int = int(anios)
	except ValueError:
		messagebox.showerror("Error", "Años de experiencia debe ser un número entero.")
		return
	linea = f"{nombre}|{especialidad}|{anios}|{sexo}|{hospital}\n"
	with open("doctoresRegistro.txt", "a", encoding="utf-8") as f:
		f.write(linea)
	messagebox.showinfo("Éxito", "Datos guardados correctamente.")
	entry_nombre.delete(0, tk.END)
	combo_especialidad.set("")
	entry_anios.delete(0, tk.END)
	combo_hospital.set("")
	var_sexo.set("")

root = tk.Tk()
root.title("Registro de Doctores")
root.geometry("350x400")

tk.Label(root, text="Nombre del doctor:").pack(anchor="w", padx=10, pady=(10,0))
entry_nombre = tk.Entry(root, width=40)
entry_nombre.pack(padx=10)


# Combobox de especialidad
tk.Label(root, text="Especialidad:").pack(anchor="w", padx=10, pady=(10,0))
combo_especialidad = ttk.Combobox(root, values=["Cardiología", "Neurología", "Pediatría", "Traumatología" ], state="readonly", width=37)
combo_especialidad.pack(padx=10)

tk.Label(root, text="Años de experiencia:").pack(anchor="w", padx=10, pady=(10,0))
entry_anios = tk.Entry(root, width=40)
entry_anios.pack(padx=10)

tk.Label(root, text="Sexo:").pack(anchor="w", padx=10, pady=(10,0))
var_sexo = tk.StringVar()
frame_sexo = tk.Frame(root)
frame_sexo.pack(anchor="w", padx=10)
tk.Radiobutton(frame_sexo, text="Masculino", variable=var_sexo, value="Masculino").pack(side="left")
tk.Radiobutton(frame_sexo, text="Femenino", variable=var_sexo, value="Femenino").pack(side="left")


# Combobox de hospital
tk.Label(root, text="Hospital donde trabaja:").pack(anchor="w", padx=10, pady=(10,0))
combo_hospital = ttk.Combobox(root, values=["Hospital central", "Hospital Norte", "Clínica Santa María", "Clínica Vida"], state="readonly", width=37)
combo_hospital.pack(padx=10)

tk.Button(root, text="Registrar", command=guardar_datos).pack(pady=20)

root.mainloop()

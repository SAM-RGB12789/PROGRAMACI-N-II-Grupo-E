import tkinter as tk
from tkinter import messagebox

###COMBO
#CREAR VENTANA PRINCIPAL
ventana=tk.Tk
ventana.title("Ejemplo Combobox")
ventana.geometry("300x200")

#Etiqueta
etiqueta=tk.Label(ventana, text="Seleccione especialidad: ")
etiqueta.grid(row=0, column=0, padx=10, pady=10, sticky= "w")

#crear combobox
opciones=["Cardiilogia", "Neurologia", "Pediatria", "Dermatologia"]
combo=ttk.combobox(ventana, values=opciones, state="readonly")
combo.current(0) #seleccionar primera opcion por defecto
combo.grid(row=0, column= 1, padx=10, pady=10)

#FUNCION PARA MOSTRAR LA SELECCION
def mostrar():
    seleccion=combo.get()
    tk.messagebox.showinfo("Sleccion", f"Has elegido{seleccion}")
#boton para confirmar seleccion
boton=tk.Button(ventana, text="Aceptar", command=mostrar)
boton.grid(row=1, column=0, columnspan=2,pady=15)


ventana.mainloop()
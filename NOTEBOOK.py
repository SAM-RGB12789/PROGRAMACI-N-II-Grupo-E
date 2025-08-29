import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#crear ventana principal
ventana_principal=tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores")
ventana_principal.geometry("400x600")

#crear contenedor de NOTEBOOK (pestañas)
pestanas=ttk.Notebook(ventana_principal)

#crear frame para pestaña pacientes (uno por pestaña)
frame_pacientes=ttk.Frame(pestanas)

#agregar pestañas al notebook
pestanas.add(frame_pacientes, text="Pacientes")

#Mostrar las pestañas en la ventana 
pestanas.pack(expand=True, fill="both")

######
#crear frame para pestaña DOCTORES (uno por pestaña)
frame_doctores = ttk.Frame(pestanas)

#agregar pestañas al notebook
pestanas.add(frame_doctores, text="Doctores")
#Mostrar las pestañas en la ventana 
pestanas.pack(expand=True, fill="both")

#NOMBRE
labelNombre=tk.Label(frame_pacientes, text="Nombre Completo")
labelNombre.grid(row=0, column=0,sticky="w", padx=5, pady=5,)
nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0, column=1,sticky="w", padx=5, pady=5)

# FECHA DE NACIMIENTO
labelFecha = tk.Label(frame_pacientes, text="Fecha de Nacimiento")
labelFecha.grid(row=1, column=0, sticky="w", padx=5, pady=5)
fechaP = tk.Entry(frame_pacientes)
fechaP.grid(row=1, column=1, sticky="w", padx=5, pady=5)

#EDAD
labelEdad=tk.Label(frame_pacientes, text="Edad: ")
labelEdad.grid(row=2, column=0, sticky="w", padx=5, pady=5)
edadP=tk.Entry(frame_pacientes, state="readonly")
edadP.grid(row=2, column=1, sticky="w", padx=5, pady=5)

#GENERO
labelGenero=tk.Label(frame_pacientes, text="Género: ")
labelGenero.grid(row=3, column=0, sticky="w", padx=5, pady=5)

genero=tk.StringVar()
genero.set("Masculino") #valor por defecto
radioMasculino=tk.Radiobutton(frame_pacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, sticky="w", padx=5, pady=5)
radioFemenino=ttk.Radiobutton(frame_pacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=4, column=1, sticky="w", padx=5)

#grupo sanguineo
labelGrupoSanguineo=tk.Label(frame_pacientes, text="Grupo Sanguíneo: ")
labelGrupoSanguineo.grid(row=4, column=0, sticky="w", pady=5, padx=5)
entryGrupoSanguineo=tk.Entry(frame_pacientes)

##TIPO DE SEGURO
labelTipoSeguro=tk.Label(frame_pacientes, text="Tipo de Seguro: ")
labelTipoSeguro.grid(row=5, column=0, sticky="w", padx=5, pady=5)
tipo_seguro=tk.StringVar()
tipo_seguro.set("Público") #valor por defecto
comboTipoSeguro=ttk.Combobox(frame_pacientes, values=["Público", "Privado", "Ninguno"], textvariable=tipo_seguro)
comboTipoSeguro.grid(row=5, column=1, sticky="w", padx=5, pady=5)

#CENTRO MÉDICO
labelCentroMedico=tk.Label(frame_pacientes, text="Centro Médico: ")
labelCentroMedico.grid(row=6, column=0, sticky="w", padx=5, pady=5)
centro_medico=tk.StringVar()
centro_medico.set("Hospital General") #valor por defecto
comboCentroMedico=ttk.Combobox(frame_pacientes, values=["Hospital General", "Clínica  Norte", "Centro Sur"], textvariable=centro_medico)
comboCentroMedico.grid(row=6, column=1, sticky="w", padx=5, pady=5)

ventana_principal.mainloop()
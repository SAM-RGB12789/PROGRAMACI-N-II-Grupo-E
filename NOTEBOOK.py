import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
 
#crear ventana principal
ventana_principal=tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores")
ventana_principal.geometry("800x600")
 
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
edadP=tk.Entry(frame_pacientes,)
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
labelCentroMedico=tk.Label(frame_pacientes, text="Centro de Salud: ")
labelCentroMedico.grid(row=6, column=0, sticky="w", padx=5, pady=5)
centro_medico=tk.StringVar()
centro_medico.set("Hospital General") #valor por defecto
comboCentroMedico=ttk.Combobox(frame_pacientes, values=["Hospital General", "Clínica  Norte", "Centro Sur"], textvariable=centro_medico)
comboCentroMedico.grid(row=6, column=1, sticky="w", padx=5, pady=5)
 
#framear botones
btn_frame=tk.Frame(frame_pacientes)
btn_frame.grid(row=8, column=0, columnspan=2, pady=5, padx=5, sticky="w")
 
#boton registrar  
btn_registrar=tk.Button(btn_frame, text="Registrar", command="")
btn_registrar.grid(row=0, column=0, padx=5)
 
#boton eliminar
btn_eliminar=tk.Button(btn_frame, text="Eliminar", command="")
btn_eliminar.grid(row=0, column=1, padx=5)
 
#crar Treeview para mostrar pacientes
treeview = ttk.Treeview(frame_pacientes, columns=("Nombre", "FechaN", "Edad", "Género", "GrupoS", "TipoS", "CentroM"), show="headings"
)
 
#Definir encabezados
treeview.heading("Nombre", text="Nombre Completo")
treeview.heading("FechaN", text="Fecha de Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Género", text="Género")
treeview.heading("GrupoS", text="Grupo Sanguíneo")
treeview.heading("TipoS", text="Tipo de Seguro")
treeview.heading("CentroM", text="Centro Médico")
 
#definir anchos de columnas
treeview.column("Nombre", width=120)
treeview.column("FechaN", width=120)
treeview.column("Edad", width=50, anchor="center")
treeview.column("Género", width=60, anchor="center")
treeview.column("GrupoS", width=100, anchor="center")
treeview.column("TipoS", width=100, anchor="center")
treeview.column("CentroM", width=120)
 
#ubicar treeview en la cuadricula  
treeview.grid(row=7, column=0, columnspan=2, padx=5, pady=10, sticky="nsew")
 
#scrollbar vertical
scroll_y=tk.Scrollbar(frame_pacientes, orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=7, column=2, sticky="ns")
 
#frame doctores
 

 
##### DOCTORES ######
# Título 
label_titulo = tk.Label(frame_doctores, text="Registro de Doctores", font=("Arial", 16, "bold"))
label_titulo.grid(row=0, column=0, columnspan=4, pady=(15, 20), sticky="nsew")

tk.Label(frame_doctores, text="Nombre:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_nombreD = tk.Entry(frame_doctores, justify="center")
entry_nombreD.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

tk.Label(frame_doctores, text="Especialidad:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
combo_especialidadD = ttk.Combobox(frame_doctores, values=["Cardiología", "Pediatría", "Neurología", "Dermatología", "General"], justify="center")
combo_especialidadD.grid(row=1, column=3, padx=5, pady=5, sticky="ew")

tk.Label(frame_doctores, text="Edad:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
spin_edadD = tk.Spinbox(frame_doctores, from_=25, to=80, width=5, justify="center")
spin_edadD.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
spin_edadD.delete(0, tk.END)
spin_edadD.insert(0, 0)

tk.Label(frame_doctores, text="Teléfono:").grid(row=2, column=2, padx=5, pady=5, sticky="e")
entry_telefonoD = tk.Entry(frame_doctores, justify="center")
entry_telefonoD.grid(row=2, column=3, padx=5, pady=5, sticky="ew")

# botones doctores
btn_frameD = tk.Frame(frame_doctores)
btn_frameD.grid(row=3, column=0, columnspan=4, pady=10)
tk.Button(btn_frameD, text="Registrar", bg="green", fg="white", width=12).grid(row=0, column=0, padx=10)
tk.Button(btn_frameD, text="Eliminar", bg="red", fg="white", width=12).grid(row=0, column=1, padx=10)

# tabla
treeview_doctores = ttk.Treeview(frame_doctores, columns=("Nombre", "Especialidad", "Edad", "Teléfono"), show="headings", height=7)
treeview_doctores.grid(row=4, column=0, columnspan=4, padx=5, pady=10, sticky="nsew")

for col in ("Nombre", "Especialidad", "Edad", "Teléfono"):
    treeview_doctores.heading(col, text=col)
    treeview_doctores.column(col, anchor="center", width=150)

for i in range(4):
    frame_doctores.grid_columnconfigure(i, weight=1)

ventana_principal.mainloop()
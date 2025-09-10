import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
#EVENTO PARA CAMBIAR DE PESTAÑA#

###------ACTUALIZACION DE LA CLASE FUNCION PARA ENMASCARAR FECHA------### 
#funcion para enmascarar fecha
def enmascarar_fecha(texto):
    limpio=''.join(filter(str.isdigit, texto)) 
    formato_final=""
    
    if len(limpio)>8:
        limpio=limpio[:8]
    if len(limpio)>4:
        formato_final=f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len(limpio)>2:
        formato_final=f"{limpio[:2]}-{limpio[2:]}"
    else:
        formato_final=limpio
    if fechaN.get() != formato_final:
        fechaN.delete(0, tk.END)
        fechaN.insert(0, formato_final)
    if len (fechaN.get())==10:
        fecha_actual=datetime.now().date()
        fecha_nacimiento=datetime.strptime(fechaN.get(), "%d-%m-%Y").date()
        edad=fecha_actual.year - fecha_nacimiento.year 
    else:
        edadVar.set("")
    return True
###--------------------- FUNCION PARA GUARDAR ARCHIVE-------------###
def guardar_en_archivo():
    with open("paciente.txt","w",encoding="utf=8") as archivo:
        for paciente in paciente_data:
            archivo.write(f"{paciente['Nombre']}|{paciente['Fecha de Nacimiento']}|{paciente['Edad']}|"f"{paciente['Genero']}|{paciente['Grupo sanguíneo']}|"f"{paciente['Tipo de Seguro']}|{paciente['Centro Médico']}\n")
#--------------------- FUNCION PARA CARGAR ARCHIVO ------------------###
def cargar_desde_archivo():
    try:
        with open("paciente.txt","r",encoding="utf=8") as archivo: ###"r" es para leer#
            paciente_data.clear() #limpiar lista antes de cargar
            for linea in archivo:
                datos=linea.strip().split("|")
                if len(datos)==7:
                    paciente={
                        "Nombre": datos[0],
                        "Fecha de Nacimiento": datos[1],
                        "Edad": datos[2],
                        "Genero": datos[3],
                        "Grupo sanguíneo": datos[4],
                        "Tipo de Seguro": datos[5],
                        "Centro Médico": datos[6]
                    }
                    paciente_data.append(paciente)
        cargar_treeview()
    except FileNotFoundError:
        open("paciente.txt","w",encoding="utf=8").close() #crear archivo si no existe
#
###--------------------- PACIENTES ------------------------------###
#lista de pacientes (inicialmente vacia)
paciente_data=[]
#funcion para registrar paciente
def registrarPaciente(): #crear diccionario con los datos ingresados
    paciente={
        "Nombre": nombreP.get(),
        "Fecha de Nacimiento": fechaN.get(),
        "Edad": edadVar.get(),
        "Genero": genero.get(),
        "Grupo sanguíneo": comboGrupoSanguineo.get(),
        "Tipo de Seguro": tipo_seguro.get(),
        "Centro Médico": centro_medico.get()
    }
    #AGREGAR PACIENTE A LA LISTA
    paciente_data.append(paciente)
    #CARGAR TREEVIEW
    guardar_en_archivo()
    #RECARGAR TREEVIEW
    cargar_treeview()
##funcion cargar treeview
def cargar_treeview():
    #limpiar treeview
    for paciente in treeview.get_children():
        treeview.delete(paciente)
    #insertar cada paciente
    for i, item in enumerate(paciente_data):
        treeview.insert("", "end", iid=str(i),values=(
            item["Nombre"],
            item["Fecha de Nacimiento"],
            item["Edad"],
            item["Genero"],
            item["Grupo sanguíneo"],
            item["Tipo de Seguro"],
            item["Centro Médico"]
        ))  
###---------------- FUNCION PARA ELIMINAR PACIENTES ----------------------###
def eliminarPaciente():
    seleccionado = treeview.selection()
    if seleccionado:
        indice = int(seleccionado[0])
        id_item = seleccionado[0]
        if messagebox.askyesno("Eliminar Paciente", "¿Estás seguro de que deseas eliminar a este paciente?"): 
            {treeview.item(id_item, 'values')[0]}
            del paciente_data[indice]
            guardar_en_archivo() #GUARDAR LOS CAMBIOS EN EL ARCHIVO
            cargar_treeview()
            messagebox.showinfo("Eliminar Paciente", "Paciente eliminado exitosamente.")
    else: ##ESTE ELSE ES DEL IF SELECCIONADO
        messagebox.showwarning("Eliminar Paciente", "No se ha seleccionado ningún paciente.")
        return        
        
#####-------------------- DOCTORES --------------------------######
##LAS FUNCIONES TXT REGISTRAR Y ELIMINAR##
def guardar_doctores_en_archivo():
    with open("paciente.txt","w",encoding="utf=8") as archivo:
        for doctor in paciente_data:
            archivo.write(f"{doctor['Nombre']}|{doctor['Especialidad']}|{doctor['Edad']}|"f"{doctor['Teléfono']}\n")
###
def cargar_doctores_desde_archivo():
    try:
        with open("doctores.txt","r",encoding="utf=8") as archivo: ###"r" es para leer#
            doctores_data.clear() #limpiar lista antes de cargar
            for linea in archivo:
                datos=linea.strip().split("|")
                if len(datos)==4:
                    doctores_data={
                        "Nombre": datos[0],
                        "Especialidad": datos[1],
                        "Edad": datos[2],
                        "Teléfono": datos[3],
                    }
                    doctores_data.append(doctores_data)
        cargar_treeview()
    except FileNotFoundError:
        open("doctores.txt","w",encoding="utf=8").close() #crear archivo si no existe
###
def eliminarDoctores():
    seleccionado2 = treeview.selection()
    if seleccionado2:
        indice = int(seleccionado2[0])
        id_item = seleccionado2[0]
        if messagebox.askyesno("Eliminar Doctor", "¿Estás seguro de que deseas eliminar a este Doctor?"): 
            {treeview.item(id_item, 'values')[0]}
            del doctores_data[indice]
            guardar_en_archivo() #GUARDAR LOS CAMBIOS EN EL ARCHIVO
            cargar_treeview()
            messagebox.showinfo("Eliminar Doctor", "Doctor eliminado exitosamente.")
    else: ##ESTE ELSE ES DEL IF SELECCIONADO
        messagebox.showwarning("Eliminar Doctor", "No se ha seleccionado ningún Doctor.")
        return  
##LAS FUNCIONES TXT REGISTRAR Y ELIMINAR##
#funcion para doctores
doctores_data = []

def registrarDoctor():
    if entry_nombreD.get() and combo_especialidadD.get() and spin_edadD.get() and entry_telefonoD.get():
        doctor = {
        "Nombre": entry_nombreD.get(),
        "Especialidad": combo_especialidadD.get(),
        "Edad": spin_edadD.get(),
        "Teléfono": entry_telefonoD.get()
    }
        doctores_data.append(doctor)
        guardar_doctores_en_archivo()
        cargar_treeview_doctores()
        messagebox.showinfo("Registro exitoso", "Doctor registrado correctamente.")
    else:
        messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")
    #
    cargar_treeview_doctores()

def cargar_treeview_doctores():
    for doctor in treeview_doctores.get_children():
        treeview_doctores.delete(doctor)
    for i, item in enumerate(doctores_data):
        treeview_doctores.insert("", "end", iid=str(i), values=(
            item["Nombre"],
            item["Especialidad"],
            item["Edad"],
            item["Teléfono"]
        )) 
###----------------- FUNCION PARA ELIMINAR DOCTORES --------------### 
def eliminarDoctor():
    seleccionado = treeview_doctores.selection()
    if seleccionado:
        item_id = seleccionado[0]
        indice = int(item_id)
        if 0 <= indice < len(doctores_data):
            del doctores_data[indice]
            cargar_treeview_doctores()
            messagebox.showinfo("Eliminado", "Doctor eliminado correctamente.")
    else:
        messagebox.showwarning("Advertencia", "Por favor, selecciona un doctor para eliminar.")
        
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
#########

# ###########
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
 
# FECHA DE NACIMIENTO ##llamnado fecha
labelFecha = tk.Label(frame_pacientes, text="Fecha de Nacimiento")
labelFecha.grid(row=1, column=0, sticky="w", padx=5, pady=5)
validacion_fecha = ventana_principal.register(enmascarar_fecha)
fechaN = ttk.Entry(frame_pacientes, validate="key", validatecommand=(validacion_fecha, "%P"))
fechaN.grid(row=1, column=1, sticky="w", padx=5, pady=5)
 
#EDAD ###actualizando
labelEdad=tk.Label(frame_pacientes, text="Edad: ")
labelEdad.grid(row=2, column=0, sticky="w", padx=5, pady=5)
edadVar = tk.StringVar()
edadP=tk.Entry(frame_pacientes, textvariable=edadVar) #state="readonly"#)
edadP.grid(row=2, column=1, sticky="w", padx=5, pady=5) 

#GENERO
labelGenero=tk.Label(frame_pacientes, text="Género: ")
labelGenero.grid(row=3, column=0, sticky="w", padx=5, pady=5)

genero=tk.StringVar()
genero.set("Masculino") #valor por defecto
radioMasculino=tk.Radiobutton(frame_pacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, sticky="w", padx=5, pady=5)
radioFemenino=ttk.Radiobutton(frame_pacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=3, column=2, sticky="w", padx=0)
 
#grupo sanguineo
labelGrupoSanguineo=tk.Label(frame_pacientes, text="Grupo Sanguíneo: ")
labelGrupoSanguineo.grid(row=4, column=0, sticky="w", pady=5, padx=5)
entryGrupoSanguineo=tk.Entry(frame_pacientes)
comboGrupoSanguineo = ttk.Combobox(frame_pacientes, values=["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"], state="readonly")
comboGrupoSanguineo.grid(row=4, column=1, sticky="w", padx=5, pady=5)
comboGrupoSanguineo.set("O+")
 
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
btn_registrar=tk.Button(btn_frame, text="Registrar", command=registrarPaciente)
btn_registrar.grid(row=0, column=0, padx=5)
 
#boton eliminar
btn_eliminar=tk.Button(btn_frame, text="Eliminar", command=eliminarPaciente)
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
tk.Button(btn_frameD, text="Registrar", command=registrarDoctor, bg="green", fg="white", width=12).grid(row=0, column=0, padx=10)
tk.Button(btn_frameD, text="Eliminar",command=eliminarDoctor, bg="red", fg="white", width=12).grid(row=0, column=1, padx=10)

# tabla
treeview_doctores = ttk.Treeview(frame_doctores, columns=("Nombre", "Especialidad", "Edad", "Teléfono"), show="headings", height=7)
treeview_doctores.grid(row=4, column=0, columnspan=4, padx=5, pady=10, sticky="nsew")

for col in ("Nombre", "Especialidad", "Edad", "Teléfono"):
    treeview_doctores.heading(col, text=col)
    treeview_doctores.column(col, anchor="center", width=150)

for i in range(4):
    frame_doctores.grid_columnconfigure(i, weight=1)
cargar_desde_archivo()#cargar datos desde el archivo al iniciar la aplicacion







ventana_principal.mainloop()
### TAREA FORMULARIO PACIENTE Y FORMULARIO DOCTOR
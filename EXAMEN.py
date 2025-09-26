import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, date
import re

ventana_principal = tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores")
ventana_principal.geometry("800x650") 

# Variables para la pestaña de Pacientes
peso_paciente = tk.StringVar() 
edadVar = tk.StringVar()
genero = tk.StringVar(value="Masculino") # Variable para el género

fechaN = None 
paciente_data = [] #lista de pacientes
doctores_data = [] #lista de doctores

###------ FUNCION PARA ENMASCARAR FECHA y CALCULAR EDAD ------### 
def enmascarar_fecha(texto):
    """
    Formatea la entrada de fecha a DD-MM-AAAA y calcula la edad en tiempo real.
    Esta función depende de las variables globales fechaN y edadVar.
    """
    # 1. Limpiar la entrada, dejando solo dígitos
    limpio = ''.join(filter(str.isdigit, texto)) 
    formato_final = ""
    
    # 2. Aplicar  DD-MM-AAAA
    if len(limpio) > 8:
        limpio = limpio[:8]
    if len(limpio) > 4:
        
        formato_final = f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len(limpio) > 2:
        
        formato_final = f"{limpio[:2]}-{limpio[2:]}"
    else:
        
        formato_final = limpio
        
    # 3. Actualizar la entrada de fecha (Entry) si el formato ha cambiado
 
    if fechaN is not None:
        if fechaN.get() != formato_final:
            fechaN.delete(0, tk.END)
            fechaN.insert(0, formato_final)
        
      
        if len(fechaN.get()) == 10:
            try:
                fecha_actual = date.today()
                fecha_nacimiento = datetime.strptime(fechaN.get(), "%d-%m-%Y").date()
                
                edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
                edadVar.set(str(edad))
            except ValueError:
                
                edadVar.set("Error") 
        else:
            edadVar.set("")
            
    return True 


###--------------------- FUNCIONES DE PERSISTENCIA PACIENTES ------------------###

def guardar_en_archivo():
    """Guarda todos los datos de los pacientes en 'paciente.txt' (8 campos)."""
 
    with open("paciente.txt", "w", encoding="utf-8") as archivo:
        for paciente in paciente_data:
            # Asegurar 8 campos en paciente.txt
            archivo.write(
                f"{paciente['Nombre']}|{paciente['Fecha de Nacimiento']}|{paciente['Edad']}|"
                f"{paciente['Genero']}|{paciente['Grupo sanguíneo']}|"
                f"{paciente['Tipo de Seguro']}|{paciente['Centro Médico']}|"
                f"{paciente.get('Peso', 'N/D')}\n"
            )

def cargar_desde_archivo():
    """Carga los datos de los pacientes desde 'paciente.txt'."""
    try:
        with open("paciente.txt", "r", encoding="utf-8") as archivo:
            paciente_data.clear()
            for linea in archivo:
                datos = linea.strip().split("|")
                
                if len(datos) >= 7:
                    paciente = {
                        "Nombre": datos[0],
                        "Fecha de Nacimiento": datos[1],
                        "Edad": datos[2],
                        "Genero": datos[3] if len(datos) > 3 else "N/D", # Asegurar que existe el campo
                        "Grupo sanguíneo": datos[4] if len(datos) > 4 else "N/D", 
                        "Tipo de Seguro": datos[5] if len(datos) > 5 else "N/D", 
                        "Centro Médico": datos[6],
                        # Nuevo campo 'Peso'
                        "Peso": datos[7] if len(datos) == 8 else "N/D" 
                    }
                    paciente_data.append(paciente)
                    
        cargar_treeview()
    except FileNotFoundError:
    
        open("paciente.txt", "w", encoding="utf-8").close()

def guardar_peso_en_archivo_adicional(paciente):
    """Guarda los datos clave del paciente, incluyendo el Peso y Género, en el archivo pacientePeso.txt."""
    linea_datos = (
        f"{paciente['Nombre']}|{paciente['Fecha de Nacimiento']}|"
        f"{paciente['Edad']}|{paciente['Grupo sanguíneo']}|"
        f"{paciente['Tipo de Seguro']}|{paciente['Centro Médico']}|"
        f"{paciente['Peso']}|{paciente['Genero']}\n" # AÑADIDO: Género
    )
    try:
        with open("pacientePeso.txt", "a", encoding="utf-8") as archivo_peso:
            archivo_peso.write(linea_datos)
    except Exception as e:
        messagebox.showerror("Error de Guardado", f"No se pudo guardar en pacientePeso.txt: {e}")

###--------------------- FUNCIONES CRUD PACIENTES ------------------------------###

def registrarPaciente():
    """Valida y añade un nuevo paciente a la lista y archivos."""
    
    paciente = {
        "Nombre": nombreP.get(),
        "Fecha de Nacimiento": fechaN.get(),
        "Edad": edadVar.get(),
        "Genero": genero.get(), # Obtener valor del RadioButton
        "Grupo sanguíneo": comboGrupoSanguineo.get(),
        "Tipo de Seguro": tipo_seguro.get(),
        "Centro Médico": centro_medico.get(),
        "Peso": peso_paciente.get()
    }
    
    # Validación
    if not all([paciente["Nombre"], paciente["Fecha de Nacimiento"], paciente["Grupo sanguíneo"], 
                paciente["Tipo de Seguro"], paciente["Centro Médico"], paciente["Peso"]]):
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos obligatorios.")
        return
        
    # Validar para que Peso sea un número
    try:
        float(paciente["Peso"])
    except ValueError:
        messagebox.showwarning("Advertencia", "El campo Peso debe ser un valor numérico válido (ej. 75.5).")
        return
        
    # Validar que edad sea un número válido
    try:
        if paciente["Edad"] == "Error" or int(paciente["Edad"]) < 0:
             messagebox.showwarning("Advertencia", "La fecha de nacimiento no es válida o es futura.")
             return
    except ValueError:
        messagebox.showwarning("Advertencia", "La edad calculada no es un número válido.")
        return

    # AGREGAR PACIENTE A LA LISTA
    paciente_data.append(paciente)
    
    # Guardar en (pacientePeso.txt) con Género
    guardar_peso_en_archivo_adicional(paciente) 
    
    # Guardaren (paciente.txt) 
    guardar_en_archivo()
    cargar_treeview()
    
    messagebox.showinfo("Registro Exitoso", f"Paciente {paciente['Nombre']} registrado y datos guardados en pacientePeso.txt.")

def cargar_treeview():
    """Actualiza el Treeview de Pacientes con los datos cargados."""
    
    for paciente in treeview.get_children():
        treeview.delete(paciente)
    
    for i, item in enumerate(paciente_data):
        treeview.insert("", "end", iid=str(i),values=(
            item["Nombre"],
            item["Fecha de Nacimiento"],
            item["Edad"],
            item["Genero"],
            item["Grupo sanguíneo"],
            item["Tipo de Seguro"],
            item["Centro Médico"],
            item.get("Peso", "N/D") 
        )) 

def eliminarPaciente():
    """Elimina el paciente seleccionado del Treeview y de la lista de datos."""
    seleccionado = treeview.selection()
    if seleccionado:

        indice = int(seleccionado[0])
        nombre_paciente = paciente_data[indice]['Nombre']
        
        if messagebox.askyesno("Eliminar Paciente", f"¿Estás seguro de que deseas eliminar a {nombre_paciente}?"): 
            # Borrar de la lista
            del paciente_data[indice]
            
            # Guardar los cambios en el archivo
            guardar_en_archivo() 
            cargar_treeview()
            messagebox.showinfo("Eliminar Paciente", "Paciente eliminado exitosamente.")
    else: 
        messagebox.showwarning("Eliminar Paciente", "No se ha seleccionado ningún paciente.")
        return 
        
#####-------------------- FUNCIONES DE PERSISTENCIA DOCTORES --------------------------######

def guardar_doctores_en_archivo():
    """Guarda todos los datos de los doctores en 'doctores.txt'."""
   
    with open("doctores.txt", "w", encoding="utf-8") as archivo:
        for doctor in doctores_data:
            archivo.write(f"{doctor['Nombre']}|{doctor['Especialidad']}|{doctor['Edad']}|{doctor['Teléfono']}\n")

def cargar_doctores_desde_archivo():
    """Carga los datos de los doctores desde 'doctores.txt'."""
    try:

        with open("doctores.txt", "r", encoding="utf-8") as archivo:
            doctores_data.clear()
            for linea in archivo:
                datos = linea.strip().split("|")
                if len(datos) == 4:
                    doctor = {
                        "Nombre": datos[0],
                        "Especialidad": datos[1],
                        "Edad": datos[2],
                        "Teléfono": datos[3],
                    }
                    doctores_data.append(doctor)
            cargar_treeview_doctores()
    except FileNotFoundError:
        open("doctores.txt", "w", encoding="utf-8").close() 

###--------------------- FUNCIONES CRUD DOCTORES ------------------------------###

def registrarDoctor():
    """Valida y añade un nuevo doctor a la lista y archivos."""

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

def cargar_treeview_doctores():
    """Actualiza el Treeview de Doctores con los datos cargados."""
    for doctor in treeview_doctores.get_children():
        treeview_doctores.delete(doctor)
    for i, item in enumerate(doctores_data):
        treeview_doctores.insert("", "end", iid=str(i), values=(
            item["Nombre"],
            item["Especialidad"],
            item["Edad"],
            item["Teléfono"]
        )) 

def eliminarDoctor():
    """Elimina el doctor seleccionado del Treeview y de la lista de datos."""
    seleccionado = treeview_doctores.selection()
    if seleccionado:
        item_id = seleccionado[0]
        
        indice = int(item_id) 
        
        if 0 <= indice < len(doctores_data):
            nombre_doctor = doctores_data[indice]['Nombre']
            if messagebox.askyesno("Eliminar Doctor", f"¿Estás seguro de eliminar a {nombre_doctor}?"): 
                del doctores_data[indice]
                guardar_doctores_en_archivo() 
                cargar_treeview_doctores()
                messagebox.showinfo("Eliminado", "Doctor eliminado correctamente.")
    else:
        messagebox.showwarning("Advertencia", "Por favor, selecciona un doctor para eliminar.")
        
# -------------------- CONFIGURACIÓN DE PESTAÑAS (NOTEBOOK) --------------------

# crear contenedor de NOTEBOOK
pestanas = ttk.Notebook(ventana_principal)

# crear frames para pestañas
frame_pacientes = ttk.Frame(pestanas)
frame_doctores = ttk.Frame(pestanas)

# agregar pestañas al notebook
pestanas.add(frame_pacientes, text="Pacientes")
pestanas.add(frame_doctores, text="Doctores")
pestanas.pack(expand=True, fill="both")

# -------------------- PESTAÑA PACIENTES --------------------

# NOMBRE
labelNombre = tk.Label(frame_pacientes, text="Nombre Completo:")
labelNombre.grid(row=0, column=0, sticky="w", padx=5, pady=5)
nombreP = tk.Entry(frame_pacientes)
nombreP.grid(row=0, column=1, sticky="w", padx=5, pady=5)

# FECHA DE NACIMIENTO
labelFecha = tk.Label(frame_pacientes, text="Fecha de Nacimiento (DD-MM-AAAA):")
labelFecha.grid(row=1, column=0, sticky="w", padx=5, pady=5)
# Registrar la función de validación 
validacion_fecha = ventana_principal.register(enmascarar_fecha)
# Definir el Entry 
fechaN = ttk.Entry(frame_pacientes, validate="key", validatecommand=(validacion_fecha, "%P"))
fechaN.grid(row=1, column=1, sticky="w", padx=5, pady=5)

# EDAD
labelEdad = tk.Label(frame_pacientes, text="Edad Calculada:")
labelEdad.grid(row=2, column=0, sticky="w", padx=5, pady=5)
edadP = tk.Entry(frame_pacientes, textvariable=edadVar, state="readonly") # readonly para edad calculada
edadP.grid(row=2, column=1, sticky="w", padx=5, pady=5) 

# GENERO
labelGenero = tk.Label(frame_pacientes, text="Género:")
labelGenero.grid(row=3, column=0, sticky="w", padx=5, pady=5)
# Utilizamos la variable 'genero' definida globalmente
radioMasculino = tk.Radiobutton(frame_pacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, sticky="w", padx=5, pady=5)
radioFemenino = ttk.Radiobutton(frame_pacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=3, column=2, sticky="w", padx=0)

# GRUPO SANGUÍNEO
labelGrupoSanguineo = tk.Label(frame_pacientes, text="Grupo Sanguíneo:")
labelGrupoSanguineo.grid(row=4, column=0, sticky="w", pady=5, padx=5)
comboGrupoSanguineo = ttk.Combobox(frame_pacientes, values=["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"], state="readonly")
comboGrupoSanguineo.grid(row=4, column=1, sticky="w", padx=5, pady=5)
comboGrupoSanguineo.set("O+")

## TIPO DE SEGURO
labelTipoSeguro = tk.Label(frame_pacientes, text="Tipo de Seguro:")
labelTipoSeguro.grid(row=5, column=0, sticky="w", padx=5, pady=5)
tipo_seguro = tk.StringVar(value="Público") 
comboTipoSeguro = ttk.Combobox(frame_pacientes, values=["Público", "Privado", "Ninguno"], textvariable=tipo_seguro)
comboTipoSeguro.grid(row=5, column=1, sticky="w", padx=5, pady=5)

# CENTRO MÉDICO 
labelCentroMedico = tk.Label(frame_pacientes, text="Centro de Salud:")
labelCentroMedico.grid(row=6, column=0, sticky="w", padx=5, pady=5)
centro_medico = tk.StringVar(value="Hospital General") 
comboCentroMedico = ttk.Combobox(frame_pacientes, values=["Hospital General", "Clínica Norte", "Centro Sur"], textvariable=centro_medico)
comboCentroMedico.grid(row=6, column=1, sticky="w", padx=5, pady=5)

# CAMPO PESO
labelPeso = tk.Label(frame_pacientes, text="Peso (kg):")
labelPeso.grid(row=7, column=0, sticky="w", padx=5, pady=5)
entryPeso = tk.Entry(frame_pacientes, textvariable=peso_paciente)
entryPeso.grid(row=7, column=1, sticky="w", padx=5, pady=5)

# Frame para botones
btn_frame = tk.Frame(frame_pacientes)
btn_frame.grid(row=8, column=0, columnspan=2, pady=15, padx=5, sticky="w")

# Botón registrar 
btn_registrar = tk.Button(btn_frame, text="Registrar Paciente", command=registrarPaciente)
btn_registrar.grid(row=0, column=0, padx=5)

# Botón eliminar
btn_eliminar = tk.Button(btn_frame, text="Eliminar Paciente", command=eliminarPaciente)
btn_eliminar.grid(row=0, column=1, padx=5)

# Treeview para pacientes
treeview = ttk.Treeview(frame_pacientes, columns=("Nombre", "FechaN", "Edad", "Género", "GrupoS", "TipoS", "CentroM", "Peso"), show="headings")

# Encabezados
treeview.heading("Nombre", text="Nombre Completo")
treeview.heading("FechaN", text="Fecha de Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Género", text="Género")
treeview.heading("GrupoS", text="Grupo Sanguíneo")
treeview.heading("TipoS", text="Tipo de Seguro")
treeview.heading("CentroM", text="Centro Médico")
treeview.heading("Peso", text="Peso (kg)") 

# Anchos de columnas
treeview.column("Nombre", width=120)
treeview.column("FechaN", width=100)
treeview.column("Edad", width=40, anchor="center")
treeview.column("Género", width=60, anchor="center")
treeview.column("GrupoS", width=70, anchor="center")
treeview.column("TipoS", width=80, anchor="center")
treeview.column("CentroM", width=120)
treeview.column("Peso", width=60, anchor="center") 


treeview.grid(row=9, column=0, columnspan=2, padx=5, pady=10, sticky="nsew")

# Scrollbar vertical 
scroll_y = tk.Scrollbar(frame_pacientes, orient="vertical", command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=9, column=2, sticky="ns")


frame_pacientes.grid_rowconfigure(9, weight=1)
frame_pacientes.grid_columnconfigure(1, weight=1)

# -------------------- PESTAÑA DOCTORES --------------------

# Título 
label_titulo = tk.Label(frame_doctores, text="Registro de Doctores", font=("Arial", 16, "bold"))
label_titulo.grid(row=0, column=0, columnspan=4, pady=(15, 20), sticky="nsew")

# Campos de entrada de Doctor
tk.Label(frame_doctores, text="Nombre:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_nombreD = tk.Entry(frame_doctores, justify="center")
entry_nombreD.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

tk.Label(frame_doctores, text="Especialidad:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
combo_especialidadD = ttk.Combobox(frame_doctores, values=["Cardiología", "Pediatría", "Neurología", "Dermatología", "General"], justify="center", state="readonly")
combo_especialidadD.grid(row=1, column=3, padx=5, pady=5, sticky="ew")
combo_especialidadD.set("General")

tk.Label(frame_doctores, text="Edad:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
spin_edadD = tk.Spinbox(frame_doctores, from_=25, to=80, width=5, justify="center")
spin_edadD.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
spin_edadD.delete(0, tk.END)
spin_edadD.insert(0, 30) 

tk.Label(frame_doctores, text="Teléfono:").grid(row=2, column=2, padx=5, pady=5, sticky="e")
entry_telefonoD = tk.Entry(frame_doctores, justify="center")
entry_telefonoD.grid(row=2, column=3, padx=5, pady=5, sticky="ew")

# Botones de doctores
btn_frameD = tk.Frame(frame_doctores)
btn_frameD.grid(row=3, column=0, columnspan=4, pady=10)
tk.Button(btn_frameD, text="Registrar Doctor", command=registrarDoctor, bg="#4CAF50", fg="white", width=15).grid(row=0, column=0, padx=10)
tk.Button(btn_frameD, text="Eliminar Doctor", command=eliminarDoctor, bg="#F44336", fg="white", width=15).grid(row=0, column=1, padx=10)

# Tabla de doctores
treeview_doctores = ttk.Treeview(frame_doctores, columns=("Nombre", "Especialidad", "Edad", "Teléfono"), show="headings", height=10)
treeview_doctores.grid(row=4, column=0, columnspan=4, padx=5, pady=10, sticky="nsew")

for col in ("Nombre", "Especialidad", "Edad", "Teléfono"):
    treeview_doctores.heading(col, text=col)
    treeview_doctores.column(col, anchor="center", width=150)


for i in range(4):
    frame_doctores.grid_columnconfigure(i, weight=1)
frame_doctores.grid_rowconfigure(4, weight=1)


cargar_desde_archivo()
cargar_doctores_desde_archivo()


ventana_principal.mainloop()
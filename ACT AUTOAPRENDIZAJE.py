import tkinter as tk
from tkinter import messagebox
from datetime import datetime, date
import re


def calcular_edad(fecha_nacimiento_str):
    try:
        nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y").date()
        hoy = date.today()
        
        edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
        return edad
    except ValueError:
        return -1


def registrar_datos():

    nombre = entry_nombre.get()

    fecha_nacimiento_str = entry_fn.get()
    

    edad_ingresada = entry_edad.get() 
    
    frecuencia_cardiaca = entry_fc.get()
    presion_sistolica = entry_pa_sistolica.get()
    presion_diastolica = entry_pa_diastolica.get()
    saturacion_oxigeno = entry_so.get()
    temperatura = entry_temp.get()
    
    # 1.1. Obtener los nuevos campos
    peso = entry_peso.get() 
    grupo_sanguineo = entry_gs.get() 
    tipo_seguro = entry_ts.get()
    centro_medico = entry_cm.get() 


    
    # Validar campos obligatorios
    if not all([nombre, fecha_nacimiento_str, peso, grupo_sanguineo, tipo_seguro, centro_medico, edad_ingresada, 
                frecuencia_cardiaca, presion_sistolica, presion_diastolica, saturacion_oxigeno, temperatura]):
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return

    # Validar formato de fecha (DD/MM/AAAA)
    if not re.match(r"\d{2}/\d{2}/\d{4}", fecha_nacimiento_str):
        messagebox.showerror("Error", "El formato de la Fecha de Nacimiento debe ser DD/MM/AAAA.")
        return

    # Calcular la edad a partir de la Fecha de Nacimiento
    edad_calculada = calcular_edad(fecha_nacimiento_str)
    if edad_calculada == -1:
        messagebox.showerror("Error", "El formato de la Fecha de Nacimiento es inválido o la fecha no es válida.")
        return
        
    try:
        # Validar que los campos numéricos sean números
        float(peso) 
        int(frecuencia_cardiaca)
        int(presion_sistolica)
        int(presion_diastolica)
        float(saturacion_oxigeno)
        float(temperatura)
        
    except ValueError:
        messagebox.showerror("Error", "Asegúrese de ingresar valores numéricos válidos para Peso y Signos Vitales.")
        return

    
    
    # Nuevos datos que se van a guardar en pacientePeso.txt
    linea_datos = (f"Nombre: {nombre} | F. Nacimiento: {fecha_nacimiento_str} | Edad: {edad_calculada} años | "
                   f"Grupo Sanguíneo: {grupo_sanguineo} | Tipo de Seguro: {tipo_seguro} | "
                   f"Centro Médico: {centro_medico} | Peso: {peso} kg\n")
    
    try:
        with open("pacientePeso.txt", "a") as file:
            file.write(linea_datos)
        messagebox.showinfo("Registro Exitoso", "Datos del paciente y peso guardados en pacientePeso.txt")
        
    except Exception as e:
        messagebox.showerror("Error de Archivo", f"No se pudo guardar el archivo: {e}")
        return

    # 4. Mostrar el resumen en la interfaz 
    resumen = (f"Registro de Signos Vitales:\n\n"
                f"Paciente: {nombre} ({edad_calculada} años, ingresó {edad_ingresada} en 'Edad')\n"
                f"Peso: {peso} kg\n" 
                f"Frecuencia Cardíaca: {frecuencia_cardiaca} lpm\n"
                f"Presión Arterial: {presion_sistolica}/{presion_diastolica} mmHg\n"
                f"Saturación de Oxígeno: {saturacion_oxigeno} %\n"
                f"Temperatura: {temperatura} °C")
    
    label_resumen.config(text=resumen)


# --- Configuración de la Ventana ---
ventana = tk.Tk()
ventana.title("Registro de Pacientes y Signos Vitales")

# Entradas
frame_campos = tk.Frame(ventana, padx=10, pady=10)
frame_campos.pack(pady=10)

# Etiqueta y entrada para el Nombre
tk.Label(frame_campos, text="Nombre del paciente:").grid(row=0, column=0, sticky="w", pady=2)
entry_nombre = tk.Entry(frame_campos)
entry_nombre.grid(row=0, column=1, pady=2)

# Etiqueta y entrada para la Fecha de Nacimiento
tk.Label(frame_campos, text="Fecha Nacimiento (DD/MM/AAAA):").grid(row=1, column=0, sticky="w", pady=2)
entry_fn = tk.Entry(frame_campos)
entry_fn.grid(row=1, column=1, pady=2)

# Etiqueta y entrada para la Edad 
tk.Label(frame_campos, text="Edad (solo numérico):").grid(row=2, column=0, sticky="w", pady=2)
entry_edad = tk.Entry(frame_campos)
entry_edad.grid(row=2, column=1, pady=2)

# Etiqueta y entrada para el Grupo Sanguíneo 
tk.Label(frame_campos, text="Grupo Sanguíneo:").grid(row=3, column=0, sticky="w", pady=2)
entry_gs = tk.Entry(frame_campos)
entry_gs.grid(row=3, column=1, pady=2)

# Etiqueta y entrada para el Tipo de Seguro 
tk.Label(frame_campos, text="Tipo de Seguro:").grid(row=4, column=0, sticky="w", pady=2)
entry_ts = tk.Entry(frame_campos)
entry_ts.grid(row=4, column=1, pady=2)

# Etiqueta y entrada para el Centro Médico
tk.Label(frame_campos, text="Centro Médico:").grid(row=5, column=0, sticky="w", pady=2)
entry_cm = tk.Entry(frame_campos)
entry_cm.grid(row=5, column=1, pady=2)

# Etiqueta y entrada para el Peso 
tk.Label(frame_campos, text="Peso (kg):").grid(row=6, column=0, sticky="w", pady=2)
entry_peso = tk.Entry(frame_campos)
entry_peso.grid(row=6, column=1, pady=2)

# Espacio para separar las partes
tk.Label(frame_campos, text="--- Signos Vitales ---").grid(row=7, column=0, columnspan=2, pady=5)


# Entradas originales de Signos Vitales
tk.Label(frame_campos, text="Frecuencia Cardíaca (lpm):").grid(row=8, column=0, sticky="w", pady=2)
entry_fc = tk.Entry(frame_campos)
entry_fc.grid(row=8, column=1, pady=2)

tk.Label(frame_campos, text="Presión Arterial Sistólica:").grid(row=9, column=0, sticky="w", pady=2)
entry_pa_sistolica = tk.Entry(frame_campos)
entry_pa_sistolica.grid(row=9, column=1, pady=2)

tk.Label(frame_campos, text="Presión Arterial Diastólica:").grid(row=10, column=0, sticky="w", pady=2)
entry_pa_diastolica = tk.Entry(frame_campos)
entry_pa_diastolica.grid(row=10, column=1, pady=2)

tk.Label(frame_campos, text="Saturación de Oxígeno (%):").grid(row=11, column=0, sticky="w", pady=2)
entry_so = tk.Entry(frame_campos)
entry_so.grid(row=11, column=1, pady=2)

tk.Label(frame_campos, text="Temperatura Corporal (°C):").grid(row=12, column=0, sticky="w", pady=2)
entry_temp = tk.Entry(frame_campos)
entry_temp.grid(row=12, column=1, pady=2)

# Botón para registrar
frame_boton = tk.Frame(ventana, pady=5)
frame_boton.pack()

boton_registrar = tk.Button(frame_boton, text="Registrar y Guardar Datos", command=registrar_datos)
boton_registrar.pack()

# Resumen
frame_resumen = tk.Frame(ventana, padx=10, pady=10)
frame_resumen.pack()

label_resumen = tk.Label(frame_resumen, text="", justify="left", font=("Helvetica", 10))
label_resumen.pack()

ventana.mainloop()
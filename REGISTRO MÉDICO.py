import tkinter as tk
from tkinter import messagebox

#Funciones para Pacientes
def nuevo_paciente():
    ventanaRegistro=tk.Toplevel(ventanaPrincipal)
    #(Toplevel) crea una nueva ventana secundaria independiente a la ventana principal
    ventanaRegistro.title("Registro Paciente")
    ventanaRegistro.geometry("600x600")
    ventanaRegistro.configure(bg="#ffffff")
    #nombre
    nombreLabel=tk.Label(ventanaRegistro,text="Nombre: ")
    nombreLabel.grid(row=0,column=0, padx=10, pady=5,sticky="w")#n=noerte,s=sur,e=este,w=oeste,we,ns
    entryNombre=tk.Entry(ventanaRegistro)
    entryNombre.grid(row=0,column=1, padx=10, pady=5,sticky="we")
    entryNombre.configure(bg="white")
    #direccion
    direccionLabel=tk.Label(ventanaRegistro,text="Dirección: ")
    direccionLabel.grid(row=1,column=0, padx=10, pady=5,sticky="w")
    entryDireccion=tk.Entry(ventanaRegistro)
    entryDireccion.grid(row=1,column=1, padx=10, pady=5,sticky="we")
    entryDireccion.configure(bg="white")
    #telefono
    telefonoLabel=tk.Label(ventanaRegistro,text="Teléfono: ")
    telefonoLabel.grid(row=2,column=0, padx=10, pady=5,sticky="w")
    entryTelefono=tk.Entry(ventanaRegistro)
    entryTelefono.grid(row=2,column=1, padx=10, pady=5,sticky="we")
    entryTelefono.configure(bg="white")
    #sexo(radiobutton)
    sexoLabel=tk.Label(ventanaRegistro,text="Sexo: ")
    sexoLabel.grid(row=3,column=0, padx=10, pady=5,sticky="w")
    sexoLabel=tk.StringVar(value="Masculino")
    #es una variable especial de tkinter que se utiliza para en lazar widgets como Radiobuttons
    rbMasculino=tk.Radiobutton(ventanaRegistro, text="Masculino", variable=sexoLabel,value="Masculino",bg="white")
    rbMasculino.grid(row=3,column=1,sticky="w")
    rbFemenino=tk.Radiobutton(ventanaRegistro, text="Femenino", variable=sexoLabel,value="Femenino",bg="white")
    rbFemenino.grid(row=4,column=1,sticky="w")
    #enfermeda BASE
    enfLabel=tk.Label(ventanaRegistro, text="Enfermedades base: ",bg="white")
    enfLabel.grid(row=5,column=0, padx=10, pady=5, sticky="w")
    diabetes=tk.BooleanVar()
    hipertension=tk.BooleanVar()
    asma=tk.BooleanVar()
    #enfermedades base (checkbutton)
    cbDiabetes=tk.Checkbutton(ventanaRegistro,text="Diabetes", variable=diabetes)
    cbDiabetes.grid(row=5,column=1,sticky="w")
    cbHipertencion=tk.Checkbutton(ventanaRegistro,text="Hipertencion", variable=hipertension)
    cbHipertencion.grid(row=6,column=1,sticky="w")
    cbAsma=tk.Checkbutton(ventanaRegistro,text="Asma", variable=asma)
    cbAsma.grid(row=7,column=1,sticky="w")
    #Funcion para registro de datos
    def registroDatos():
        enfermedades=[]
        if diabetes.get():
            enfermedades.append("Diabetes")
        if hipertension.get():
            enfermedades.append("Hipertencion")
        if asma.get():
            enfermedades.append("Asma")
        
        #accion regsitrar datos
        
        if len(enfermedades)>0:
            enfermedadesTexto=",".join(enfermedades)
        else:
            enfermedadesTexto="Ninguna"
        info=(
            f"Nombre:{entryNombre.get()}\n"
            f"Direccion: {entryDireccion.get()}\n"
            f"telefono: {entryTelefono.get()}\n"
            f"sexo: {sexoLabel.get()}\n"
            f"Enfermedades: {enfermedadesTexto}"
        )
        messagebox.showinfo("Datos Registrados",info)
        ventanaRegistro.destroy() #cierra la ventana tras el mensaje
#fuera regsitrar datos
    btnRegistrar=tk.Button(ventanaRegistro, text="Datos Resgistrados", command=registroDatos)
    btnRegistrar.grid(row=9, column=0, columnspan=2, pady=15)    
        
        
def buscar_paciente():
    messagebox.showinfo("Buscar Paciente", "Buscar paciente en la base de datos.")

def eliminar_paciente():
    messagebox.showinfo("Eliminar Paciente", "Eliminar paciente del sistema.")

# Funciones para Doctores
def nuevo_doctor():
    ventanaRegDoc=tk.Toplevel(ventanaPrincipal)    
    ventanaRegDoc.title("Registro de Doctores")     
    ventanaRegDoc.geometry("400x400")     
    ventanaRegDoc.configure(bg="white")     
    #nombre     
    nombreLabel=tk.Label(ventanaRegDoc,text="Nombre:",bg="white")     
    nombreLabel.grid(row=0,column=0,padx=10,pady=5,sticky="n")     
    entryNombre=tk.Entry(ventanaRegDoc)     
    entryNombre.grid(row=0,column=1,padx=10,pady=5,sticky="we")     
    #Direccion     
    direccionLabel=tk.Label(ventanaRegDoc,text="Direccion:",bg="white")     
    direccionLabel.grid(row=1,column=0,padx=10,pady=5,sticky="n")     
    entryDireccion=tk.Entry(ventanaRegDoc)     
    entryDireccion.grid(row=1, column=1,padx=10,pady=5,sticky="we")     
    #Telefono     
    telefonoLabel=tk.Label(ventanaRegDoc,text="Telefono:",bg="white")     
    telefonoLabel.grid(row=2,column=0,padx=10,pady=5,sticky="n")     
    entryTelefono=tk.Entry(ventanaRegDoc)     
    entryTelefono.grid(row=2,column=1,padx=10,pady=5,sticky="we")     
    #sexo (radiobutton)     
    sexoLabel=tk.Label(ventanaRegDoc,text="Sexo:",bg="white")     
    sexoLabel.grid(row=3,column=0,padx=10,pady=5,sticky="n")     
    sexo=tk.StringVar="Masculino"     
    rbMasculino=tk.Radiobutton(ventanaRegDoc,text="Masculino",variable=sexo,value="Mascul ino")     
    rbMasculino.grid(row=3,column=1,sticky="n")     
    rbFemenino=tk.Radiobutton(ventanaRegDoc,text="Femenino",variable=sexo, value="Femenino")     
    rbFemenino.grid(row=4,column=1,sticky="n")     
    #Especialidad     
    especialidadLabel=tk.Label(ventanaRegDoc,text="Especialidad:",bg="white")     
    especialidadLabel.grid(row=5,column=0,sticky="n")     
    entryEspecialidad=tk.Entry(ventanaRegDoc)     
    entryEspecialidad.grid(row=5,column=1,padx=10,pady=5,sticky="we")

def buscar_doctor():
    messagebox.showinfo("Buscar Doctor", "Buscar doctor en la base de datos.")

def eliminar_doctor():
    messagebox.showinfo("Eliminar Doctor", "Eliminar doctor del sistema.")

# Ventana principal
ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("Sistema de Registro de Pacientes")
ventanaPrincipal.geometry("600x400")
ventanaPrincipal.configure(bg="#ffffff")

# Barra de menú
barraMenu = tk.Menu(ventanaPrincipal)
ventanaPrincipal.configure(menu=barraMenu)

# Menú Pacientes
menuPacientes = tk.Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Pacientes", menu=menuPacientes)
menuPacientes.add_command(label="Nuevo Paciente", command=nuevo_paciente)
menuPacientes.add_command(label="Buscar Paciente", command=buscar_paciente)
menuPacientes.add_command(label="Eliminar Paciente", command=eliminar_paciente)
menuPacientes.add_separator()
menuPacientes.add_command(label="Salir", command=ventanaPrincipal.quit)

# Menú Doctores
menuDoctores = tk.Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Doctores", menu=menuDoctores)
menuDoctores.add_command(label="Nuevo Doctor", command=nuevo_doctor)
menuDoctores.add_command(label="Buscar Doctor", command=buscar_doctor)
menuDoctores.add_command(label="Eliminar Doctor", command=eliminar_doctor)
menuDoctores.add_separator()
menuDoctores.add_command(label="Salir", command=ventanaPrincipal.quit)

# Menú Ayuda
menuAyuda = tk.Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)
menuAyuda.add_command(label="Acerca de", command=lambda: messagebox.showinfo("Acerca de", "Versión 1.0 - Sistema Biomedicina"))





ventanaPrincipal.mainloop()


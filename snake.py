import tkinter as tk
import random

ANCHO = 400
ALTO = 400
TAM_CUADRO = 20

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Simple")
        self.canvas = tk.Canvas(root, width=ANCHO, height=ALTO, bg="black")
        self.canvas.pack()
        self.boton_reiniciar = tk.Button(root, text="Reiniciar", command=self.reiniciar)
        self.boton_reiniciar.pack(pady=5)
        self.root.bind("<KeyPress>", self.cambiar_direccion)
        self.iniciar_juego()

    def iniciar_juego(self):
        self.direccion = "Right"
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.comida = self.nueva_comida()
        self.jugando = True
        self.mover()

    def reiniciar(self):
        self.canvas.delete("all")
        self.iniciar_juego()

    def nueva_comida(self):
        while True:
            x = random.randrange(0, ANCHO, TAM_CUADRO)
            y = random.randrange(0, ALTO, TAM_CUADRO)
            if (x, y) not in self.snake:
                return (x, y)

    def mover(self):
        if not self.jugando:
            self.canvas.create_text(ANCHO//2, ALTO//2, text="¡Game Over!", fill="red", font=("Arial", 24))
            return

        cabeza_x, cabeza_y = self.snake[0]
        if self.direccion == "Up":
            nueva = (cabeza_x, cabeza_y - TAM_CUADRO)
        elif self.direccion == "Down":
            nueva = (cabeza_x, cabeza_y + TAM_CUADRO)
        elif self.direccion == "Left":
            nueva = (cabeza_x - TAM_CUADRO, cabeza_y)
        else:
            nueva = (cabeza_x + TAM_CUADRO, cabeza_y)

        if (nueva[0] < 0 or nueva[0] >= ANCHO or
            nueva[1] < 0 or nueva[1] >= ALTO or
            nueva in self.snake):
            self.jugando = False
            self.mover()
            return

        self.snake = [nueva] + self.snake
        if nueva == self.comida:
            self.comida = self.nueva_comida()
        else:
            self.snake.pop()

        self.dibujar()
        self.root.after(100, self.mover)

    def dibujar(self):
        self.canvas.delete("all")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x+TAM_CUADRO, y+TAM_CUADRO, fill="green")
        x, y = self.comida
        self.canvas.create_oval(x, y, x+TAM_CUADRO, y+TAM_CUADRO, fill="red")

    def cambiar_direccion(self, event):
        tecla = event.keysym
        if tecla == "Up" and self.direccion != "Down":
            self.direccion = "Up"
        elif tecla == "Down" and self.direccion != "Up":
            self.direccion = "Down"
        elif tecla == "Left" and self.direccion != "Right":
            self.direccion = "Left"
        elif tecla == "Right" and self.direccion != "Left":
            self.direccion = "Right"

if __name__ == "__main__":
    root = tk.Tk()
    juego = SnakeGame(root)
    root.mainloop() 
    
    
    
##############
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
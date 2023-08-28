import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
CORREGIDO 
Apellido : Glinka 
Nombre : Paulo
Adivina el número (v 1.0):
Al comenzar el juego generamos un número secreto del 1 al 100, en la pantalla del juego dispondremos de un cuadro de texto 
para ingresar un número y un botón “Verificar”, si el número ingresado es el mismo que el número secreto se dará por terminado
 el juego con un mensaje similar a este: 

En esta oportunidad el juego evaluará tus aptitudes a partir de la cantidad de intentos, por lo cual se informará lo siguiente:
    1° intento: “usted es un Psíquico”.
	2° intento: “excelente percepción”.
	3° intento: “Esto es suerte”.
	4° hasta 6° intento: “Excelente técnica”.
	Más de 6 intentos: “afortunado en el amor!!”.

de no ser igual se debe informar si 
“falta…”  para llegar al número secreto  o si 
“se pasó…”  del número secreto.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        self.txt_numero = customtkinter.CTkEntry(master=self)
        self.txt_numero.grid(row=0, column=1)
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.numero_secreto = random.randrange(1, 100)
        self.numero_intento = 0
        print(self.numero_secreto)



    def btn_mostrar_on_click(self):
        
        self.numero_intento = self.numero_intento + 1
        numero_generado = self.numero_secreto
        numero_ingresado = int(self.txt_numero.get())
        if(self.numero_intento > 5):
            mensaje = "perdiste, pasaste tus 6 intentos "
        elif (numero_generado == numero_ingresado):
            mensaje = "Ganaste "
            match (self.numero_intento) :
                case 1:
                        mensaje =f"Usted es un Psiquico {mensaje} en el intento {self.numero_intento}"
                case 2:
                        mensaje = f"Exelente Percepcion {mensaje} en el intento {self.numero_intento}"
                case 3:
                        mensaje = f"Esto es Suerte {mensaje} en el intento {self.numero_intento}"
                case 4 | 5 | 6 :
                        mensaje = f"Exelente tecnica {mensaje} en el intento {self.numero_intento}"
                case _:
                        mensaje = f"Afortunado en el amor {mensaje} en el intento {self.numero_intento}"
                        
        elif (numero_ingresado < numero_generado):
                mensaje = "falta para llegar al numero "
        else :
            mensaje = "Te pasaste "
        
        alert(title="adivine el numero", message= mensaje)
        
        self.txt_numero.delete(0,100000) 
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
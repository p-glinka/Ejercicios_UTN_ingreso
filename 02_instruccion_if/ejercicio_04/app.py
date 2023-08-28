import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Paulo 
apellido: Glinka 
---
Ejercicio: instrucion_if_04
---
Enunciado:
Al presionar el botón  'Calcular', se deberá obtener contenido en la caja de texto txtEdad, 
transformarlo en número y calcular si es mayor, menor o adolescente (edad entre 13 y 17 años) 
de edad, se deberá informar utilizando el Dialog aler.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        edad_str = self.txt_edad.get()
        edad_int = int(edad_str)
        if(edad_int > 18):
            estado_mayor_menor_adolec = "MAYOR"
        elif(edad_int > 12 and edad_int < 17):
           estado_mayor_menor_adolec = "ADOLESENTE"
        else:
            estado_mayor_menor_adolec = "MENOR"
         
        alert(title="ejercicio_2.4", message = estado_mayor_menor_adolec )  
             
            

    
if __name__ == "__main__":
    app = App()
    app.mainloop()
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Paulo
apellido: Glinka
---
Ejercicio: instrucion_if_07
---
Enunciado:
Los argentinos nativos y por opción desde los dieciséis (16) años y los argentinos naturalizados desde los dieciocho (18) años están habilitados a votar. 
Al presionar el botón  'Calcular', se deberá informar (utilizando el Dialog Alert) si es o no posible que la persona concurra a votar en base a la información 
suministrada.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Tipo")
        self.label2.grid(row=1, column=0, padx=20, pady=10)

        self.combobox_tipo = customtkinter.CTkComboBox(master=self, values=["NATIVO", "NATURALIZADO"])
        self.combobox_tipo.grid(row=1, column=1, padx=20, pady=10)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        tipo_nacionalidad = self.combobox_tipo.get()
        edad_ingresada = self.txt_edad.get()
        edad_ingresada_int = int(edad_ingresada)
        if(edad_ingresada_int > 16 and tipo_nacionalidad == "NATIVO") or (edad_ingresada_int > 18 and tipo_nacionalidad == "NATURALIZADO"): 
            mensaje = "Puede Votar"
        else:
            mensaje = "No pordes votar "
        mensaje_para_el_usuario = "Usted es {0} y tiene {1} años, por lo tanto, {2}".format(tipo_nacionalidad, edad_ingresada_int, mensaje)
        
        alert(title="ejercicio 2.7", message=mensaje_para_el_usuario)
        
    
if __name__ == "__main__":
    app = App()
    app.mainloop()
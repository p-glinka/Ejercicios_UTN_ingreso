import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Apellido : Glinka
Nombre : Paulo
Entregado 
Enunciado:
Al presionar el botón ‘Validar letra’, mediante prompt solicitar al usuario que ingrese una letra. 
Se deberá validar que la letra sea ‘U’, ‘T’ o ‘N’ (en mayusculas) 
En caso no coincidir con ninguna de las letras, volverla a solicitar hasta que la condición se cumpla
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_validar_letra = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_validar_letra_on_click)
        self.btn_validar_letra.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_validar_letra_on_click(self):
        letra_ingresada = prompt(title="numero ingresado", prompt="Ingrese una letra valida" )    
        while (letra_ingresada != "U" and letra_ingresada != "T" and letra_ingresada != "N"): 
            alert(title="validacion", message="ingrese una letra valida ")
            letra_ingresada = prompt(title="Ingrese U o T o N ", prompt="ingrese una letra correcta ") 
            
        alert(title="validacion", message= "Saliste")
            
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
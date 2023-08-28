import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Apellido: Glinka
Nombre: Paulo 
Al presionar el botón Mostrar pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contador_pares = 0
        valor_ingresado = prompt(title="ingrese un valor",prompt="ingrese un valor")
        for indice in range(1,int(valor_ingresado)+1):
            print(indice)
            resultado_modulo=indice % 2
            if int(resultado_modulo) == 0:
                alert(title="numeros pares", message=f"{indice} es un numero par ")
                contador_pares += 1
        alert(title="", message= f"la cantidad de numeros pares es {contador_pares}")
            
            
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
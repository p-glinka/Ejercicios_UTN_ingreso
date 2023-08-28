import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Apellido : Glinka 
Nombe: Paulo

Al presionar el botón Mostrar pedir valores por prompt hasta que el usuario ingrese el valor 9 (se deberá utilizar 'BREAK').
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        for indice in range(20000):
            salida = prompt(title="Salga con el 9", prompt="ingrese un numero")
            if salida == "9":
                break
        alert(title="saliste", message= "apretaste el numero 9")
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
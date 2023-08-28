import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contador_divisores = 0
        valor_ingresado = prompt(title="ingrese un valor",prompt="ingrese un valor")
        valor_ingresado_int = float(valor_ingresado)
        for indice in range(1,valor_ingresado_int**0.5 +1):
            if float(valor_ingresado) % indice  == 0  and float(valor_ingresado) < 2:
                print("no es primo")
            else:
                print(f"{valor_ingresado} es primo")
                
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
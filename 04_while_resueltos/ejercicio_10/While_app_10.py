import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Alumno : Paulo 
Apellido : Glinka 
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        numero_ingresado = ""
        acumulador_positivos = 0
        acumulador_negativos = 0
        contador_pos = 0
        contador_neg = 0
        contador_0 = 0
        diferencia_catidad_positivos_negativos = 0

        
        while(numero_ingresado != None):
            numero_ingresado = prompt(title="ingrese numero", prompt="ingresa un numero")
            if(numero_ingresado != None):
                numero_ingresado_int = int(numero_ingresado)
                if(numero_ingresado_int > 0):
                    acumulador_positivos += numero_ingresado_int
                    contador_pos +=1
                elif( numero_ingresado_int < 0):
                    acumulador_negativos += numero_ingresado_int
                    contador_neg +=1
                else:
                    contador_0 +=1
                
        print(acumulador_negativos)
        print(acumulador_positivos)
        print(contador_0)
        diferencia_catidad_positivos_negativos = abs(contador_pos-contador_neg)
        mensaje = f"la suma acumulada de numeros negativos es: {acumulador_negativos} \n"
        mensaje += f"la suma acumulada de numeros positivo es: {acumulador_positivos} \n"
        mensaje += f"la cantidad de numeros negativos es: {contador_neg} \n"
        mensaje += f"la difenrecia de los positivos ingresados y los negativos es {diferencia_catidad_positivos_negativos} "
        mensaje += f"la cantidad de 0 ingresados es {contador_0}"
        alert("mensaje resurltado", message= mensaje)
        
        
                
                


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

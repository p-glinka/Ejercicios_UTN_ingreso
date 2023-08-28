'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        for postulante in range(10):
            nombre_postulante = prompt("nombre postulante ", prompt="Ingrese el nombre del postulante")
            while nombre_postulante == None:
                nombre_postulante = prompt(title="ERROR", prompt="Ingrese un nombre ")
            
            edad_postulante =prompt ("edad postulante")
            while edad_postulante != None or int(edad_postulante) < 18:
                edad_postulnte = prompt(title="ERROR", prompt="Ingrese una edad Valida")
            edad_postulante_int = int(edad_postulante)
            
            genero = prompt(title= "Genero F M NB", prompt="ingrese el Sexo")
            while genero == None or genero != "F" or  genero != "M"  or genero != "NB":
                genero= prompt(title="ERROR", prompt="Ingrese un sexo valido")
                .
                
            tecnoligias_manejadas = prompt(title="tecnologias", prompt="ingrese PYTHON - JS - ASP.NET")
            while tecnoligias_manejadas == None or tecnoligias_manejadas != "PYTHON" or tecnoligias_manejadas != "JS" or tecnoligias_manejadas != "ASP.NET":
                tecnoligias_manejadas = prompt(title= "ERROR", prompt= "ingrese una tecnologia valida (PYTHON - JS - ASP.NET)")
            puesto_aspirado = prompt(title="Puesto", prompt= "ingrese el puesto al que aspira")
            
            while puesto_aspirado == None or puesto_aspirado != "Jr" or puesto_aspirado != "Ssr" or puesto_aspirado != "Sr":
                puesto_aspirado = prompt(title="ERROR INGRESE Jr, Ssr, Sr ", prompt= "ingrese un puesto valido")
            
                
                    
            
                


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

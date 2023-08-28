import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Apellido : Glinka
Nombre : Paulo
Enunciado:

Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos
    
    nivel A:
    i. el listado de numeros pares
    j. que se ingreso mas ?, positivos , negativos o ceros

    nivel Ninja:
    k. el listado de los numeros mayores , si es que hay mas de un mayor

Informar los resultados mediante alert()

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
        columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
        columnspan=2, sticky="nsew")

        self.lista = []

    def btn_comenzar_ingreso_on_click(self):
        
        while True:
            elemento = prompt("ingreso de numeros ", prompt="ingrese un numero")
            if elemento == None:
                break
            else:
                self.lista.append(int(elemento))
            

    def btn_mostrar_estadisticas_on_click(self):
        suma_negativos=0
        suma_positivos=0
        contador_positivos=0
        contador_negativos=0
        contador_ceros=0
        minimo_negativos=None
        maximo_posivos=None
        promedio_negativos=0
        numeros_pares= []
        lista_de_mayores = []
        
        for numero in self.lista: 
            resultado_modulo=numero % 2 
            if int(resultado_modulo) == 0:
                numeros_pares.append(numero)
            if numero > 0:
                suma_positivos += numero
                contador_positivos += 1
                if maximo_posivos == None or  numero > maximo_posivos:
                    maximo_posivos = numero
                    lista_de_mayores = []
                    lista_de_mayores.append(maximo_posivos)
                elif numero == maximo_posivos:
                    lista_de_mayores.append(maximo_posivos)
                    
            elif numero < 0:
                suma_negativos += numero
                contador_negativos += 1
                if minimo_negativos == None or numero < minimo_negativos:
                    minimo_negativos = numero
            else: 
                contador_ceros += 1 
        if contador_positivos > contador_negativos and contador_positivos > contador_ceros: 
            mayor_cantidad_pnc= "Son mas positivos"
        elif contador_negativos > contador_ceros:
            mayor_cantidad_pnc= "Son mas negativos"
        else:
            mayor_cantidad_pnc = "Son mas 0"
            

        promedio_negativos=suma_negativos/contador_negativos
        

        
        alert(title="mensaje",message= f"la suma acumulada de negativos es {suma_negativos}, la suma de positivos es {suma_positivos},se ingresaron {contador_positivos} numeros positivos, {contador_negativos} numeron negativos, {contador_ceros} ceros, el minino negativo fue {minimo_negativos} y el maximo positivo fue {maximo_posivos}, el pormedio de los numeros negativos fue {promedio_negativos} los numeros pares fueron {numeros_pares}, {mayor_cantidad_pnc} el numero mayor se repitio {lista_de_mayores}")
            
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

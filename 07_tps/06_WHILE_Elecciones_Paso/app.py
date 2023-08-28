'''
Apellido : Glinka 
Nombre : Paulo 
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
e. se pide ingresar el sexo (M , F , NB) , informar cuantos candidatos hay de cada sexo

f. se pide ingresar nivel de aceptacion de imagen del candidato (entre -100 y 100) informar el
nombre y sexo del que mejor nivel tiene 

g.de las personas de sexo femenino ,informar cuanta hay mayores a 50 y cuantas menores a esa edad

h. de que sexo hubo mas candidatos
Todos los datos se ingresan por prompt y los resultados por consola (print)

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
        max_votos = None
        min_votos = None
        contador_edad = 0
        suma_edad_candidatos = 0
        total_de_votos_emitidos = 0
        sexo_masculino = 0
        sexo_femenino = 0
        sexo_nb = 0
        imagen_mas_alta = None
        contador_mayor_fem = 0
        contador_menor_fem = 0
        sexo_max_candidatos = None
        
                    # Ingreso Datos
        while  True:
            
            nombre_candidato = prompt("Nombre candidato", prompt="ingrese el nombre del candidato")
            while nombre_candidato == None or not  nombre_candidato.isalpha():
                nombre_candidato = prompt("Error ", prompt="Reingrese el nobre del candidato  ")
                
            
            edad_candidato = prompt("ingrese edad del candidato ", prompt="ingrese la edad del candidato ")
            while edad_candidato == None or int(edad_candidato) < 25:
                edad_candidato = prompt("Error ", prompt="Reingrese Numero ")
            edad_candidato_int = int(edad_candidato)
            # Apartado (c)
            suma_edad_candidatos += edad_candidato_int
            contador_edad += 1
            
            cantidad_de_votos = prompt(title="ingrese la cantidad de votos", prompt="ingrese la cantidad de votos ")
            while cantidad_de_votos == None or int(cantidad_de_votos) < 0:
                cantidad_de_votos = prompt(title="Error", prompt="ingrese un valor valido ")
            cantidad_de_votos_int = int(cantidad_de_votos)
            # Apartado d
            total_de_votos_emitidos += cantidad_de_votos_int          
            
            # Apartado (a)
            
            if max_votos == None or cantidad_de_votos_int > max_votos:
                max_votos = cantidad_de_votos_int
                nombre_max_votos = nombre_candidato
                
            # Apartado (b)
            
            if min_votos == None or cantidad_de_votos_int < min_votos:
                min_votos = cantidad_de_votos_int
                nombre_min_votos = nombre_candidato
                edad_min_votos = edad_candidato_int
                
            # Apartado e
            sexo_cantidato=prompt(title="Sexo cantidato", prompt="Ingrese el sexo del candidato (F, M, NB)")
            while sexo_cantidato == None or sexo_cantidato != "F" and sexo_cantidato != "M" and sexo_cantidato != "NB":
                sexo_cantidato = prompt(title="ERROR", prompt= "Ingrese un Sexo Valido: F , M, NB")
            
            match sexo_cantidato:
                case "M":
                    sexo_masculino += 1
                case "F":
                    sexo_femenino += 1
                    edad_candidata_fem = edad_candidato_int
                    if edad_candidata_fem > 50: 
                        contador_mayor_fem += 1
                    else:
                        contador_menor_fem += 1
                case "NB":
                    sexo_nb = +1
                    
            
            
                    
            #apartado f
            nivel_aceptacion = prompt(title="ingrese el nivel de aceptacion del candidato", prompt="ingrese un valor entre -100 y 100")
            while True:
                if -100 <= int(nivel_aceptacion) <= 100:
                    nivel_aceptacion_int = int(nivel_aceptacion)
                    break
                else:
                    nivel_aceptacion = prompt(title="error", prompt="ingrese un valor validos")
            if imagen_mas_alta == None or nivel_aceptacion_int > imagen_mas_alta:
                imagen_mas_alta = nivel_aceptacion_int
                nombre_candidato_imagen_mas_alta = nombre_candidato
                edad_candidato_imagen_mas_alta = edad_candidato_int
            
                
            result = question(title="nuevo candidato?", message="Desea ingresar un nuevo candidato?")
            if result == False:
                break
            
            
        # Proceso de datos    

        
        promedio_edad_candidatos = suma_edad_candidatos / contador_edad
        
        # Apartado h
        
        if sexo_masculino > sexo_femenino and sexo_masculino > sexo_nb:
            sexo_mayor_candidatos = "Maculino"
        elif sexo_femenino > sexo_nb:
            sexo_mayor_candidatos = "Femenino"
        else:
            sexo_mayor_candidatos = "No Binario"
        
        
        print("Nombre del candidato con mas votos fue {0}  ".format(nombre_max_votos)) 
        print("El nombre de candidato con menos votos fue, {0}, y su edad es {1} años ".format(nombre_min_votos, edad_min_votos))
        print("El promedio de edades de los candidatos es {0} años ".format(promedio_edad_candidatos))
        print("La suma total de votos emitidos es {0}".format(total_de_votos_emitidos))
        print("De los candidatos ingresados {0} fueron masculinos, {1} fueron femeninos, {2} fueron de sexo no binario".format(sexo_masculino, sexo_femenino, sexo_nb))
        print("El nombre del candidato con imagen mas alta es {0}, y su edad es {1}".format(nombre_candidato_imagen_mas_alta, edad_candidato_imagen_mas_alta))
        print("De las candidatas femeninas {0} son mayores a 50 años y {1} son menores a esa edad ".format(contador_mayor_fem, contador_menor_fem))
        print("Hubo Mayor cantidad de candidartos de sexo {0} ".format(sexo_mayor_candidatos))
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

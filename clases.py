
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import pandas as pd


class Mat:
    def __init__(self) -> None:
        self.mat={}
        

    def ingresarMat(self,direccion,mat):
        self.mat[direccion]=sio.loadmat(mat)


    def ver_mat(self):
        for clave,valor in self.mat.items():
            print(f"clave {clave} : valor {sio.whosmat(clave)}")
    
    def graficar_Mat(self):
            contador= 0
            for i in self.mat.items():
                contador+=1
                print(f"{contador}.calve: {i[0]} : {sio.whosmat(i[0])}")
            while True:
                try:
                    
                    select= input("\nIngrese la clave de la matriz que desea graficar:")
                    cargar= sio.loadmat(select)
                    nombre= input("\ningrese nombre de la matriz a graficar:")
                    sub= int(input("\nIngrese el canal que desea graficar:"))
                    inicio= int(input( "Inicio de la muestra a graficar:"))
                    final= int(input("Final de muestra a graficar:"))
                    columna= int(input("Epoca:")) 

                    señal= cargar[nombre] 
                    señal1= señal[sub,inicio:final,columna]
                    plt.figure(figsize=(15, 15))
                    plt.subplot(2,4,2)
                    plt.boxplot(señal1)
                    plt.title('Boxplot')
                    plt.xlabel('Tiempo')
                    plt.ylabel('Amplitud')
                    plt.grid(True)
                    
                    print()
                    eje=int(input("Ingrese a lo largo de que eje desea hacer le promedio\n0.eje 0 \n1.eje 1\n2.eje 2\n"))
                    fila= int(input("Ingrese fila a promediar"))
                    colum_i= int(input("Ingrese inicio de la columna a graficar"))
                    colum_f= int(input("Ingrese final de la columna a graficar"))
                    promedio= np.mean(señal,eje)
                    
                    plt.subplot(2,4,5)
                    plt.plot(promedio[fila,colum_i:colum_f])
                    plt.title("Promedio:")
                    plt.xlabel('Tiempo')
                    plt.ylabel('Amplitud')
                    plt.grid(True)

                    print("Suma de sensores")

                    sub1= int(input("Ingrese el canal que desea graficar:"))
                    inicio1= int(input( "Muestra inicial:"))
                    final1= int(input("Muestra final:"))
                    columna1= int(input("epoca a graficar:")) 
                    señal2=señal[sub1,inicio1:final1,columna1]

                    # sub2= int(input("Ingrese el canal que desea graficar:"))
                    canal2= int(input("Ingrese otro canal a graficar")) 
                    señal3= señal[canal2,inicio1:final1,columna1]

                    suma = señal2 + señal3
                    ruido = np.random.normal(0, 0.2, suma.shape)  # Incremento de la desviación estándar del ruido
                    suma_con_ruido = suma + ruido
                    tiempo_ms = np.linspace(inicio1, final1, len(suma_con_ruido))

                    plt.subplot(2, 4, 8)
                    plt.plot(tiempo_ms, suma_con_ruido)
                    plt.title('Suma de dos sensores con ruido')
                    plt.xlabel('Tiempo (ms)')
                    plt.ylabel('Amplitud')
                    plt.grid(True)
                    plt.show()

                    plt.show()
                    break
                except ValueError:
                    print("¡Valor invalido, intente de nuevo!")

class Csv:
    def __init__(self) -> None:
        self.csv= {}

    def ingresar_CSV(self, nombreArchivo):
        csv_content = pd.read_csv(nombreArchivo)
        self.csv[nombreArchivo] = csv_content
        
    def mostrarInformacion(self):
            contador=0
            for i in self.csv.keys():
                contador+=1
                print(f"{contador}. clave: {i}")
            inicio= input("Ingrese la clave del archivo csv que desea graficar:")
            csv2= self.csv.get(inicio)
            print("El archivo CSV contiene las siguientes columnas:")
            for col in csv2.columns:
                print(col)
            
            selected_column = input("Ingrese el nombre de la columna a graficar: ")
            plt.figure(figsize=(10, 5))
            plt.subplot(1,2,1)
            plt.hist(csv2[selected_column], label=selected_column)
            plt.title('Gráfico de señal - Archivo CSV')
            plt.xlabel('Tiempo')
            plt.ylabel('Amplitud')
            plt.legend()
            plt.grid(True)

            print("Suma de columnas")

            col1= input("Ingrese nombre de columna a sumar")
            col2= input("Ingrese nombre de columna a sumar")
            señalCol= csv2[col1]
            señalCol1= csv2[col2]
            suma1= señalCol+señalCol1
            plt.subplot(1,2,2)
            plt.boxplot(suma1)
            plt.title('Gráfico de la suma  - Archivo CSV')
            plt.xlabel('Tiempo')
            plt.ylabel('Amplitud')
            plt.grid(True)
            plt.show()







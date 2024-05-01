from clases import *


mat=Mat()
csv=Csv()


def main():
    while True:
        try:
            print("Menu:\n")
            print("1.Ingresar mat\n2.Ingresar csv\n3.Graficar señal\n4.Mostrar informacion\n5.Salir")
            entrada= int(input("Ingrese una opcion:"))
            if entrada==1:
                direccion= input("Ingrese la direccion del archivo:")
                mat.ingresarMat(direccion,direccion)

            if entrada==2:
                direccion=input("Ingrese la direccion del archivo:")
                csv.ingresar_CSV(direccion)
            if entrada==3:
                print(mat.graficar_Mat())
            if entrada==4:
                print(csv.mostrarInformacion())

            if entrada==5:
                break
        except (ValueError, FileNotFoundError,AttributeError):
            print("¡Valor invalido, intente de nuevo!")
main()




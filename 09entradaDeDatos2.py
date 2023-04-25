nombre=input("ingrese su nombre: ")
print("hola "+nombre+"vamos a realizar una suma.")

numUno= int(input("ingrese el numero 1: "))
numDos= int(input("ingrese el numero 2: "))

resultado= numUno+numDos
#! se concatena con la , para evitar convertir un str a int y no agregar una linea extra
print(nombre + "el resultado de la suma es: ", resultado)
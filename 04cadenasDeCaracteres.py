
mensaje="Hola"
mensaje +=" "
mensaje +="Brandon"
print(mensaje)

print("\nConcatenacion")
mensaje="Hola"
espacio=" "
nombre="Brandon"
print(mensaje+espacio+nombre)

numeroUno=4
numeroDos=2
resultado=numeroUno+numeroDos
#!se debe convertir un string a entero 
#! como en la linea 16 por que intenta tomar lo de arriba osea un string y no int
resultado= str(resultado)  
print("\nel resultado de la suma es: "+resultado)

#*buscar subcadena con el metodo find 
print("\nbusqueda")
mensaje="Hola Brandon"
buscarSubcadena=mensaje.find("Brandon")
print(buscarSubcadena)

#*extraccion buscar por posicion por  ejemplo[1:8] el 1 es la
#*posicion inicial y el 8 es hasta donde

print("\nExtraccion")
extraerCadena=mensaje[1:8]
print(extraerCadena)

#* igualacion
print("\ncomparacion")
mensajeUno= "hola"
mensajeDos= "hola"
print( mensajeUno==mensajeDos)



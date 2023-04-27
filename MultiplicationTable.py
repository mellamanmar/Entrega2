# Crear un programa que imprima en pantalla una tabla de multiplicar utilizando un ciclo for.

num= int(input ("Ingrese el número de la tabla que desea conocer "))
tabla= []
if num > 0:
    for i in range (20):
        multiplicacion= i*num
        tabla.append(multiplicacion)
print (tabla)

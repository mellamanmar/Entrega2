# Crear un programa que reciba una lista de palabras y muestre únicamente aquellas que empiezan con una letra determinada, utilizando un ciclo for y una estructura condicional if.

lista= []
for i in range (5):
    palabra= input ("Ingrese una palabra: ") .lower()
    lista.append (palabra)
print (lista)    

for palabra in lista:
    if palabra[0] == "l":
        print (palabra)

print ("Fin del programa")
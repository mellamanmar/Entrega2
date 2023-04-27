
#Crear un programa que reciba dos listas de números y que genere una tercera lista que contenga la suma de los elementos de las dos listas en la misma posición, utilizando un ciclo for.

list1= []
for i in range (3):
    num1= int (input ("Ingrese un número para la primera lista: "))
    list1.append(num1)
print (list1)

list2= []
for i in range (3):
    num2= int (input ("Ingrese un número para la segunda lista: "))
    list2.append(num2)
print (list2)

list3= []
for i in range(len(list2)):
    suma= list1[i]+list2[i]
    list3.append(suma)
print (list3)
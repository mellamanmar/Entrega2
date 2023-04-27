#Crear un programa que reciba una lista de números y calcule la suma de los mismos utilizando un ciclo for.

list1= []
for i in range (5):
    num1= int(input("Ingrese el primer número: "))
    list1.append (num1)
list2= []
for i in range (5):
    num2= int(input ("Ingrese el segundo número: "))
    list2.append (num2)

print ("La lista 1 es: ", list1, "La lista 2 es: ", list2)

for i in list1:
    list1_suma1= i+i
    print (list1_suma1)
print (sum(list1))

for i in list2:
    list2_suma1= i+i
    print (list2_suma1)
print (sum(list2))

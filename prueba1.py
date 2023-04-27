#Bucle de resta de un número hasta que no se cumpla

num= float(input ("Ingresa un número: "))
while num > 0:
    num= num + 1
    print (num)
    if num >= 10:
        break
        print ("Supera el límite")
print ("Listo")

#Bucle for para los números del 1 al 6

i=1
for i in range (1,6):
    print (i)
else:
    print ("Haz terminado")

#Bucle para lista de frutas

fruits= ["apple", "banana", "cherry"]
for i in fruits:
    print (i)
else:
    print ("Cómpralas")
    
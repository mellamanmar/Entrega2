#Hacer una lista de frutas y mostrarlas por pantalla, luego mostrar letra por letra estas frutas

frutas= []
for i in range (5):
    print ("Ingrese una fruta para una lista de compras")
    valor= input() .upper()
    frutas.append(valor)

for i in frutas:
    print ("Debes comprar",i)

print (frutas)
for i in frutas:
    for indice in i:
        print (indice)
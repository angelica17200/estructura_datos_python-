# EJERCCIOS LISTAS 

#Ejerccios manipulación 

# 1.  consiste en la definicion de una lista con el elementis de diferentes tipos y mostrala por pantalla, 
# entera como por elementos accedienod a la posición que ocupa dentro de la lista.

lista=["Python", "Guanenta", 2022, "Libro",3]
print(lista)
print(lista[0])
print(lista[2])

# 2.  consiste en el uso del operador + para realizar uniones de listas. Además, 
# utilizar la funcion len para conocer el número de elemento que compone la lista.

lista=["camiseta", "pantalon","zapatillas"]
lista2=["abrigo", "jersey ","sudadera","calcetines"]

print("lista1:",lista)
print("Número elementos lista2:", len(lista2))
print("lista2:",lista2)
lista_concatenada= lista +lista2
print("Número elementos lista:_concatenada", len(lista_concatenada))
print("lista_concatenada:",lista_concatenada)

# 3. Añaddir elementos a la lista de diferentes formas 

lista=["camiseta", "pantalon","zapatillas"]
print(lista)
lista=lista + ["Abrigo"]
print(lista)
lista=lista+["Jersey","Sudadera"]
print(lista)
lista=lista+["Calcetines"]+["Bufanda"]
print(lista)

# 4. Modificar elemntos de una lista u borrar elementos de la misma.
lista=["camiseta", "pantalon","zapatillas"]
print(lista)
lista[1]="cazadora"
print(lista)
del lista[0]
print(lista)

# 5. uso del operador * , que permite concatenar una ista con ella misma un número finito de veces

lista=["camiseta", "pantalon","zapatillas"]
print(lista)
lista_resultante=lista*3
print(lista_resultante)

# 6.  creación de lista como elemntos de listas y accesos de dichos elementos.
print("----Ejercicio 6-----")
lista=["camiseta",["calcetines","cazadora"], "zapatillas"]
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[1][0])
print(lista[1][1])

# 7. Extraer una porcion de la lista en una lista nueva.

print("----Ejercicio 7-----")
lista=[1,2,3,4,5,6,7,8,9]
print(lista)
lista1 = lista[3:7]
print(lista1)
lista2=lista[:5]
print(lista2)
lista3=lista[6:]
print(lista3)


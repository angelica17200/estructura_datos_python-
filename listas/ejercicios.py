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

lista1=["camisa", "pantalon","zapatillas"]
lista2=["abrigo", "jersey ","sudadera","calcetines"]

print("lista1:",lista1)
print("Número elementos lista2:", len(lista2))
print("lista2:",lista2)
lista_concatenada= lista1 +lista2
print("Número elementos lista:_concatenada", len(lista_concatenada))
print("lista_concatenada:",lista_concatenada)

# 3. Añaddir elementos a la lista de diferentes formas 

lista=["camisa", "pantalon","zapatillas"]
print(lista)
lista=lista + ["Abrigo"]
print(lista)
lista=lista+["Jersey","Sudadera"]
print(lista)
lista=lista+["Calcetines"]+["Bufanda"]
print(lista)

# 4. Modificar elemntos de una lista u borrar elementos de la misma.
lista1=["camisa", "pantalon","zapatillas"]
print(lista)
lista[1]="cazadora"
print(lista)
del lista[0]
print(lista)
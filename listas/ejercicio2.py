# EJERCCIOS LISTAS 

# Métodos propios

lista=[45,32,3,78]
# funcion append:añade un elemento a la lista
print("Lista original",lista)
lista.append(995)
lista.append(7)
print("Lista despues de usar append:" , lista)
# Función sort: ordena la alista 
lista.sort()
print("Lista ordenada:", lista)
# Función reverse:invierte el ordden de la lista 
lista.reverse()
print("Lista al revés:",lista )
# Función extend: añade los elementos de un lista a la lista.
lista_extend =[1,5,87,45]
lista.extend(lista_extend)
print("Lista despues de extend:", lista )
# Función count: cuenta el numero de veces  que aparece el elemento indicado como parametro dentro de la lista.
print("Número de elementos 45:",lista.count(45))
#Función insert: añade el elemento pasado como parametro a la lista en la posición indicada tambien por parametros
lista.insert(4,111)
print("Lista despues de insert:", lista)
# Función remove: elimina la primera ocurrencia empenzando por la izquierda de la lista del elemnto inidcado como parámetro.
lista.remove(45)
print("Lista despues de remove:", lista)
#Función index: devuelve la primera posición de la primera ocurrencia de izquierda a derecha en lalista, del elemento pasado como parámetro.
print("Posición del elemento 11:", lista.index(111))
#Funciín pop: elimina un elemento de la lista y lo devuelve como resultado de la operación.
lista.pop()
print("Lista despues de pop:", lista )
# Función clear: elimina los elementos de la lista.
lista.clear
print("Lista despues de clear:", lista)



# EJERCCIOS Diccionarios 

#Ejercicio de Manipulación

#1.vamos arealizar referentes a diccionario
#será crear uno y mostrar algunos elementos del mismo.
#Para acceder alos elemntos del diccionario deberás utlizare la clave.

diassemanaingles = {"Lunes":"Monday", "Martes": "Tuesday", "Miercoles":"Wednesday", "Jueves": "Thursday", "viernes":"Friday"}
print(diassemanaingles["Lunes"])
print(diassemanaingles["Miercoles"])
print(diassemanaingles["Viernes"])

#2. Añadimos los días sábado y domingo, modificando el valor de lagún 
# elemnto y borrandoalgun elemento.

diassemanaingles = {"Lunes":"Monday", "Martes": "Tuesday", "Miercoles":"Wednesday", "Jueves": "Thursday", "viernes":"Friday"}
print(diassemanaingles)
diassemanaingles [ "Sabado"] = "Saturday"
print(diassemanaingles)
diassemanaingles ["Domingo"] = "Sunday"  
print(diassemanaingles)
diassemanaingles [ "Lunes"] = "MondayBORRAR"  
print(diassemanaingles)
del diassemanaingles["Lunes"]
print(diassemanaingles)

#3. utlizar las funciones de len, max y min.

diassemanaingles = {"Lunes":"Monday", "Martes": "Tuesday", "Miercoles":"Wednesday", "Jueves": "Thursday", "viernes":"Friday"}
print("Númerode elementos del diccionario:",len(diassemanaingles))
print("elemento mayor del diccionario;",max(diassemanaingles ))
print("elemento mayor del diccionario;",min(diassemanaingles ))
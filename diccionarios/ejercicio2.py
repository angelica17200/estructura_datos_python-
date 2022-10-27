# EJERCCIOS Diccionarios 

# METODOS PROPIOS 

# Función de copy: Realiza una copia exacta del diccionario en uno nuevo.
diassemanaingles = {"Lunes":"Monday", "Martes": "Tuesday", "Miercoles":"Wednesday", "Jueves": "Thursday", "viernes":"Friday"}
print("Dicccionario original ",diassemanaingles)
diccionariocopia =diassemanaingles.copy()
print("Diccionario copy:",diccionariocopia)
#Función de pop: obteniene el valor de la clave pasada comoparámetro y además elimina 
# el elemento del diccionario.
print("Valor del Lunes (pop):", diassemanaingles.pop("Lunes "))
print ("Diccionario después del pop:",diassemanaingles)
#Función de popitem: obtiene un elemento aleatorio del diccionario y lo eleimina del mismo.
print("Elemento ala azar con popitem:",diassemanaingles )
# Función  de get: obtoiene el valor de la clave pasada como parámetro.
print("valor del Martes (get):(no existe):",diassemanaingles.get("Martes"))
print("valor del Lunes (get):(no existe):",diassemanaingles.get("Lunes"))
print("valor del Lunes (get):(no existe):",diassemanaingles.get("Lunes"," No existe"))
#Funcion  de update: una actualizancion utlizando otro diiccionario.
diassemanaingles.update({"Lunes":"MondayNUEVO","Mrtes":"TuesdayNUEVO"})
#FUNCION DE SETDEFAUL: intenta insertar un elemento (clave y valor ) en el diccionorio en caso de no existir dicho elemento.
print("setefault del Sabado:", diassemanaingles.setdefault ("Sabado","Sabado","Saturday"))
print("Diccionario después del setdefaul: ", diassemanaingles.setdefault("Lunes","Lunes")")
print("setdefault de Sabado:, ",diassemanaingles.setdefault("Sabado","Sabado","Saturday"))
print("Diccionario después del update: (elemento existente): ",diassemanaingles)
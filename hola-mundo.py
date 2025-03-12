# Puedo realizar un comentario, usando gato. Para indicar la funcionalidad de mi código. 
# Esta línea de código (no. 3) me sirve para imprimir un texto
print("hola mundo")

print("Mi nombre es Luis Castaño, tengo 23 años")

#Texto
print(type("Hola mundo"))
#Número entero
print(type(5))
#Número décimal 
print(type(12.52))

"""
En Python se pueden manejar muchos tipos de datos o variables. Los tipos de datos es como reconoce la computadora los valores que le estas dando. 

- string (cadenas de texto)
- float (números flotantes)
- boleanos (falso o verdadero)
- enteros
- listas
- diccionarios
- sets
"""

#concatenar 2 cadenas de texto
print("hola" + " sumo otro texto")
print("Tengo " + str(23) + " años")
Hola = "Hola"
Mundo = "mundo"
print("Este es el resultado de concatenar usando join() la siguiente frase:"," ".join([Hola,Mundo]))

# Le pide al usuario su nombre y su edad
nombre = str(input("Dime, ¿cuál es tu nombre? \n"))
edad=int(input("Cual es tu edad \n "))
print("Un saludo para "+ nombre+ ",tu edad es de " + str(edad) )

# suma de 2 números enteros
n1 = 20 # defino las variables
n2 = 25
ntot = n1 + n2 # sumo ambos números
print(type(ntot)) #comunico cual es el tipo de dato, del total de la suma de 2 números enterosl

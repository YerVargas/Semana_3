frutas = ("Manzana", "Banano", "Cereza")

nombres = ["Ana", "Luis", "Carlos"]

numeros = [12,24,35]

"""for fruta in frutas: #sirve para listas y tuplas
    print(fruta)"""

"""for i in range(4): # el rango 4, imprime d 0 a 3, q es el numero antes del 4
    print(i)"""
    
# puedo anidar los for

for nombre, fruta in zip(nombres,frutas): #zip me sirve para tener dos listas o tuplas, va recorriendo uno a 1: frutas 1 nombres 1, frutas 2 nombres 2 y asi
   print(f"{nombre} tiene una {fruta}.") 
   
for numero in numeros:
    resultado = numero*2
    print(f"El doble de {numero} es {resultado}")
    
for i in range(len(nombres)):
    print(nombres[i])
    
for q in enumarate(frutas): #enumarate me sirve para acceder a los datos con indice y valor ya q me devuelve un conjunto cn la info en ese orden
    indice = q[0]
    valor = q[1]
    print(q[0]) #me imprime el indice de la lista 0,1,2
    print(q[1]) #me imprime los valores de la lista manzana, banano, cereza
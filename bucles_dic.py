diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

for key in diccionario: #no puedo acceder a los datos solo a la clave
    #key
    print(f"la clave es {key}")
    
for datos in diccionario.items(): #puedo acceder a datos y claves
    clave = datos[0]
    valor = datos[1]
    print(datos)
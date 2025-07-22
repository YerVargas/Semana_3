frutas = ["manzana","pera","banana","cereza"]

for fruta in frutas:
    if fruta == "cereza":
        #print("Encontre una cereza, continuaré")
        continue #me evita la fruta q le estoy indicando pero me muestra las demas
    print(f"Fruta:{fruta}")
    
for fruta in frutas:
    print(f"Fruta:{fruta}")
    if fruta == "pera":
        break   #me detiene el bucle cuando encuentre la fruta q le indiqué, si se ejecuta se sale por completo, no se cumple el else
else:
    print("No se econtro la banana")
    
print("No se encontro la banan se recorrio todo el codigo")
    
    
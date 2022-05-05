
print("Inserte una cadena de texto:")
cadena1 = input()
print("Inserte otra cadena de texto:")
cadena2 = input()
combinaciones = []


for i in cadena1:
    for j in cadena2:
        combinaciones.append(i+j)


print('Estas son las combinaciones entre', cadena1, 'y', cadena2)
print(" ".join(combinaciones))
print("Número de combinaciones:", len(combinaciones))

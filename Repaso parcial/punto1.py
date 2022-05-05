a=()#Inicialización de una variable tipo tupla
a=tuple((int(input('Ingrese x del punto A: ')),int(input('Ingrese y del punto A: '))))

b=()
b=tuple((int(input('Ingrese x del punto B: ')),int(input('Ingrese y del punto B: '))))

distance=((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
print('La distancia entre A y B es', distance)


#Casting de string hacia los valores que conforman la tupla
#  print(type(a))#confirmando el tipo de variable a
#  print(type(a[0]))

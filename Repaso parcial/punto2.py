print('Ingrese la distancia que hay entre los dos carros (se asume que está expresada en metros):')
d = float(input())
print('Ingrese la velocidad del carro A (se asume que está expresada en m/s):')
a = float(input())
print('Ingrese la velocidad del carro B (se asume que está expresada en m/s):')
b = float(input())

crash = d/(a+b)
print('Se estima que ambos carros se estrellarán', crash, 'segundos')

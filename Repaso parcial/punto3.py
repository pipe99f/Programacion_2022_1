
print('Ingresa un mensaje:')
mensaje = input()
print('Ingresa clave de codificación (cualquier entero diferente a 0):')
clavecod = int(input())
mlist = list(mensaje)
emlist = []

for i in mlist:
    a = chr(ord(i) + clavecod)
    emlist.append(a)

print('El mensaje codificado es:\n' + ''.join(emlist))




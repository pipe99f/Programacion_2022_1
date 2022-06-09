def admindict():
    a = 'y'
    dict = {}
    contador = 0
    while a == 'y':
        subdict = {}
        print('Ingrese tres datos')
        for i in range(1,4):
            subdict[f'dato{i}'] = input(f'Dato {i}: ')
        dict[contador] = subdict
        a = input('Desea continuar? (y/n) ')
        contador += 1
    print('Primer usuario: \n', dict[0], '\nÚltimo usuario: \n', dict[contador-1])

admindict()

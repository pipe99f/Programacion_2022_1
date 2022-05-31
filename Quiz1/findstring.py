#String a buscar: CATGAGCAGTGCTGACTCAACTCAGGCCTAA

g = 'CATGAGCAGTGCTGACTCAACTCAGGCCTAA'
with open("/home/pipe99g/ve/prog/python/Programacion_2022_1/Quiz1/sequence_Covid-19.fasta") as f:
    lines = f.readlines()

secuence=''
for l in lines[1:]:
    secuence+=l[:-1]
#  print(secuence)

contador = 0
#algoritmo buscador
for i in secuence:
    flag = 0
    subcont = 0
    for a in range(3):
        subcont += 1
        if secuence[contador+a] != g[a]:
            flag = 1
            break
        elif secuence[contador + len(g)-a-1] != g[-a-1]:
            flag = 1
            break
    if flag == 0:
        if g == secuence[contador:contador+len(g)]:
            print("El fragmento se encuentra en la posición:", contador)
            break
        else:
            contador += 1
    elif flag == 1:
        contador += 1


problema='CATGAGCAGTGCTGACTCAACTCAGGCCTAA'
a=secuence.find(problema)
print(a)

import json
import requests 
from pprint import pprint

response = requests.get(
        "https://fp.josedomingo.org/lmgs/u05/ej2.json"
        )
pruebas = json.loads(response.text)
pprint(pruebas)

def numeropruebas():
    count = 0
    for i in pruebas:
        count +=1
    return count

#  print(f"Hay {numeropruebas()} pruebas")

def pruebas_mas_de_dos_horas():
    titulos = []
    for i in pruebas:
        if i["Horas"] > 2:
            titulos.append(i["Titulo"])
    return titulos

#  print(pruebas_mas_de_dos_horas())

def pruebas_no_presenciales():
    url = []
    for i in pruebas:
        if i["TipoFormacion"] != "Presencial":
            url.append(i["URL"])
    return url
#  print(pruebas_no_presenciales())

def profesor_y_titulo(ID):
    tituloyprofesor = []
    nombres = []
    for i in pruebas:
        if i["ID"] == ID:
            for a in i['Profesorado']:
                nombres.append(a['NombreCompleto'])
            tituloyprofesor.append(i['Titulo'])
            tituloyprofesor.append(nombres)
            break
    return tituloyprofesor
#  print(profesor_y_titulo('A15050007'))

def prof_titulos_dict():
    tituloyprofesor = {}
    nombres = []
    for i in pruebas:
        nombres = []
        for a in i['Profesorado']:
            nombres.append(a['NombreCompleto'])
        tituloyprofesor[i['Titulo']] = nombres
    return tituloyprofesor
print(prof_titulos_dict())

with open("Titulos y profesores.json", 'w') as jsonfile:
    json.dump(prof_titulos_dict(), jsonfile)





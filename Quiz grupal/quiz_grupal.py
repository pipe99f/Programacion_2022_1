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

print(pruebas_mas_de_dos_horas())

def pruebas_no_presenciales():
    url = []
    for i in pruebas:
        if i["TipoFormacion"] != "Presencial":
            url.append(i["URL"])
    return url
print(pruebas_no_presenciales())

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
print(profesor_y_titulo('A15050007'))

def profesor_y_titulo_sin_ID():
    tituloyprofesor = []
    nombres = []
    for i in pruebas:
        sublista = []
        for a in i['Profesorado']:
            nombres.append(a['NombreCompleto'])
        sublista.append(nombres)
        sublista.append(i['Titulo'])
        tituloyprofesor.append(sublista)
return tituloyprofesor
print(profesor_y_titulo_sin_ID())

def prof_y_titulo_to_dict():
    list = profesor_y_titulo_sin_ID
    for i in list:
        list[i[0]]: i[[1]]





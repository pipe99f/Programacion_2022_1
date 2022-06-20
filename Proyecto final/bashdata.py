import json
import os
import subprocess

def getAudioSources():
    with os.popen("pactl get-default-sink") as dO:
        defaultOutput = dO.read()[:-1]+".monitor" #[:-1] borra el salto de línea

    with os.popen("pactl get-default-source") as dI:
        defaultInput = dI.read()[:-1]
    with os.popen("pactl list sources | grep Name") as srces:
        audioSources = srces.read()


    for i in ["\t", "\n", "Name:"]: #Con esta iteraciión elimino los tabs, saltos de línea y strings "Name:"
        audioSources = audioSources.replace(i, "")
    sources = []
    for i in audioSources.split(" "):
        if i != defaultInput and i!= defaultOutput and i: #"and i" para evitar que en las lista hayan strings vacíos
            sources.append(i)
    return defaultInput, defaultOutput, sources

defaultInput, defaultOutput, sources = getAudioSources()

# print(defaultOutput)
# print(defaultInput)
# print(sources)

# def getOutputs():
#     with os.popen("swaymsg -t get_outputs | ") as dO:
#         defaultOutput = dO.read()[:-1] #[:-1] borra el salto de línea
def getOutputs():

    defaultOutput = subprocess.check_output(["swaymsg", "-t", "get_outputs"])
    return [o["name"] for o in json.loads(defaultOutput)]
getOutputs()
screens = getOutputs()
# print(getOutputs())
#
def getDate():
    date = subprocess.check_output(['date', '+"%d_%b_%H:%M"'])
    return date.decode()[1:-2] #[1:-2] elimina las comillas
# print(getDate())


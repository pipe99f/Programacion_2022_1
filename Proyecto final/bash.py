import json
import os
import subprocess

def getAudioSources():
    with os.popen("pactl get-default-sink") as dO:
        defaultOutput = dO.read()[:-1] #[:-1] borra el salto de línea

    with os.popen("pactl get-default-source") as dI:
        defaultInput = dI.read()[:-1]
    with os.popen("pactl list sources | grep Name") as srces:
        audioSources = srces.read()


    for i in ["\t", "\n", "Name:"]: #Con esta iteraciión elimino los tabs, saltos de línea y strings "Name:"
        audioSources = audioSources.replace(i, "")
    sources = []
    for i in audioSources.split(" "):
        if (i != defaultInput or i!= defaultOutput) and i: #"and i" para evitar que en las lista hayan strings vacíos
            sources.append(i)
    return defaultInput, defaultOutput, sources

defaultInput, defaultOutput, sources = getAudioSources()

print(defaultOutput)
print(defaultInput)
print(sources)

# def getOutputs():
#     with os.popen("swaymsg -t get_outputs | ") as dO:
#         defaultOutput = dO.read()[:-1] #[:-1] borra el salto de línea
def getOutputs():
    """
    Returns a list of all available outputs via `swaymsg -t get_outputs`, e.g.:
    ['eDP-1', 'HDMI-A-1']
    """
    defaultOutput = subprocess.check_output(["swaymsg", "-t", "get_outputs"])
    return [o["name"] for o in json.loads(defaultOutput)]
getOutputs()
print(getOutputs())


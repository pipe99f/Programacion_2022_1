import os
with os.popen("pactl get-default-sink") as dO:
    defaultOutput = dO.read()[:-1]

with os.popen("pactl get-default-source") as dI:
    defaultInput = dI.read()[:-1]


print (defaultOutput)
print (defaultInput)

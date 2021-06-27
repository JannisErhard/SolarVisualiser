#!/usr/bin/env python3
import csv
import matplotlib.pyplot as plt
import sys


#file auswählen, header als liste initialisiern
filename = str(sys.argv[1])
header=[]
x=[]
y=[]
#magischen csv reader nehmen um datei einzulesen
with open(filename) as file:
    content = csv.reader(file, delimiter = ",", quotechar = '"')
    content = [x for x in content]

#schreib alles bis "voltage" in den header
for i in range(len(content)):
    header.append((content[i][0], content[i][1]))
    if content[i][0] == " Voltage:    ":
        xlabel=content[i][0]
        ylabel=content[i][1]
        break
#damit 1 zeile nach "voltage" in floats umgewandelt wird
i=i+1
j=i
#alle relevanten daten werden geprintet als float bis die leere zeile kommt
for i in range(i,len(content)):
    if len(content[i]) != 2:
        break
    x.append(float(content[i][0]))
    y.append(float(content[i][1]))

plt.plot(x,y)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.show()


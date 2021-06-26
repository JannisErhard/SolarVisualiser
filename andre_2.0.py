#!/usr/bin/env python3
import csv
import matplotlib.pyplot as plt
import sys


#file auswählen, header als liste initialisiern
filename = str(sys.argv[1])
left=[]
right=[]
x=[]
y=[]
#magischen csv reader nehmen um datei einzulesen
file=open(filename,"r")
lines=file.readlines()

#schreib alles bis "voltage" in den header

for line in lines:
    if line == "\n":
        right.append("Empty_Line")
        left.append("Empty_Line")
    else:
       left.append(((line.strip().split(","))[0]).strip())
       right.append(((line.strip().split(","))[1].strip()))
file.close()

startpoint=left.index("Voltage:")
endpoint=left.index("Empty_Line")

xlabel=left[startpoint]
ylabel=right[startpoint]
for i in range(startpoint+1,endpoint):
    x.append(float(left[i]))
    y.append(float(right[i]))


plt.plot(x,y)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.show()
print(len(x),len(y))


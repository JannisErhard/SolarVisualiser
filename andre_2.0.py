#!/usr/bin/env python3
import matplotlib.pyplot as plt
import sys


#file auswählen, header als liste initialisiern
filename = str(sys.argv[1])
left=[]
right=[]
x=[]
y=[]

def read_and_parse_current_file(filename):
    '''Open, Read and Parse file filename'''
    
    file=open(filename,"r")
    lines=file.readlines()
    
    for line in lines:
    # if line is empty, add element that can be identified later in
        if line == "\n":
            right.append("Empty_Line")
            left.append("Empty_Line")
        else:
    # in case of normal line 
#           left.append(((line.strip().split(","))[0]).strip())
#           right.append(((line.strip().split(","))[1].strip()))
           left.append(((line.split(","))[0]).strip())
           right.append(((line.split(","))[1].strip()))
    file.close()
    return left, right

left, right = read_and_parse_current_file(filename)

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


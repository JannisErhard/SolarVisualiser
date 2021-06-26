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
    '''Open, Read and Parse file filename. Output left and right column of file.'''
    
    file=open(filename,"r")
    lines=file.readlines()
    
    for line in lines:
    # if line is empty, add element that can be identified later in
        if line == "\n":
            right.append("Empty_Line")
            left.append("Empty_Line")
        else:
    # in case of normal line, split at "," get rid of blanks 
           left.append(((line.split(","))[0]).strip().replace(":",""))
           right.append(((line.split(","))[1].strip()).replace(":",""))
    file.close()
    return left, right

def get_ordinate_and_coordinate(left,right):
    '''Take left and right column of quatsch file and extract data. Output xlabel,ylabel,ordinate,coordinate'''
    startpoint=left.index("Voltage")
    endpoint=left.index("Empty_Line")
    
    xlabel=left[startpoint]
    ylabel=right[startpoint]
    for i in range(startpoint+1,endpoint):
        x.append(float(left[i]))
        y.append(float(right[i]))
    return xlabel, ylabel, x, y

def read_header_into_dict(left,right):
    '''Reads the header of ``quatsch'' - Files into dictionary'''
    endpoint=left.index("Voltage")
    header = {}
    for i in range(0,endpoint):
        header[str(left[i])]=right[i]
    return header 

left, right = read_and_parse_current_file(filename)
xlabel, ylabel, x, y = get_ordinate_and_coordinate(left,right)
header = read_header_into_dict(left,right)



plt.plot(x,y)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(header['Title'])
#print(header.keys())
#print(header.values())
plt.show()


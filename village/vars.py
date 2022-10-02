

#read in data from rosalind
text = open("rosalind_ini2.txt","rt")
data=text.read()
text.close()

data = data.split(" ")

import numpy as np



a = int(data[0])
b = int(data[1])


hyp = (a*a + b*b)
print(hyp)

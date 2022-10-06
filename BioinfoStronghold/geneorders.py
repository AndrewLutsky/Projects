import numpy as np
import itertools as it
text = open("Rosalind_perm.txt","rt")
data = text.read()
text.close()


data.split(" ")
var = int(data[0])
fact = np.math.factorial(var)
list = [None] * fact
print(fact)

l1=[]
for i in range(var):
    l1.append(i+1)

l2 = it.permutations(l1)
for i in l2:
    for j in i:
        if j == i[-1]:
            print(j,end="\n")
        else:
            print(j,end=" ")
        

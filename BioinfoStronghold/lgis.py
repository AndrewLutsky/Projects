import numpy as np
import math
from itertools import combinations

text = open("rosalind_lgis.txt","rt")
data = text.read()
text.close()

data = data.split('\n')
length = int(data[0])
permutationGiven = data[1].split(' ')
for i in range(0, len(permutationGiven)):
    permutationGiven[i] = int(permutationGiven[i])


#finds the index of a given value
def findIndex (listUnsorted, a):
    for i in range(0, len(listUnsorted)):
        if a == listUnsorted[i]:
            return i



#dynamic programming solution

path = [] 
for i in range(len(permutationGiven)):
    path.append([permutationGiven[i]])
    for j in range(i):
        if permutationGiven[i] > permutationGiven[j]:
            if len(path[i]) <= len(path[j]):
                path[i] = path[j] + [permutationGiven[i]]
pathLength = [0] * len(path)
for i in range(0, len(path)):
    pathLength[i] = len(path[i])

maxIndex = findIndex(pathLength, max(pathLength))

for i in path[maxIndex]:
    print(i, end=" ")

print("")


path = [] 
for i in range(len(permutationGiven)):
    path.append([permutationGiven[i]])
    for j in range(i):
        if permutationGiven[i] < permutationGiven[j]:
            if len(path[i]) <= len(path[j]):
                path[i] = path[j] + [permutationGiven[i]]
pathLength = [0] * len(path)
for i in range(0, len(path)):
    pathLength[i] = len(path[i])
maxIndex = findIndex(pathLength, max(pathLength))

for i in path[maxIndex]:
    print(i, end=" ")







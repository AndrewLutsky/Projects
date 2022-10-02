
#Import dataset from Rosalind
text = open("rosalind_grph.txt","rt")
data = text.readlines()
text.close()


#create dictionary of accession number and sequence data
keys = []    
values = []    
    
count = -1    
for line in data:    
    if line[0] == ">":    
        keys.append(line[1:].strip('\n'))    
        count += 1    
        values.append("")    
    if line[0] != ">":    
        values[count] += line.strip('\n')    
        
dict = dict(zip(keys,values))    

def isEdge(s,t):
    
    suffix = s[-3:]
    prefix = t[0:3]
    if suffix == prefix:
        return True
    else:
        return False

        



for i in keys:
    for j in keys:
        if dict[i] != dict[j]:
            if isEdge(dict[i],dict[j]) == True:
                print(i,j)




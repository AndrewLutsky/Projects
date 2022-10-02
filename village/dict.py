#reads in data from rosalind    
text= open("rosalind_ini6.txt","rt")    
data = text.read()    
text.close()    


dict = {}
for word in data.split(" "):    
    word = word.strip('\n')
    if word in dict.keys():
        dict[word] += 1
    elif word not in dict.keys():
        dict[word] = 1

for keys, values in dict.items():
    print(keys,values)

#values = []
#
#for i in range(len(data)):
#    keys.append(i)
#    values.append(0)
#
#dict = dict(zip(keys,values))
#
#for i in range(len(data)):
#    for j in range(len(data)):
#        if data[i] == data[j] and i !=j:
#            dict[i] = dict[i] + 1
#
#
#print(dict)

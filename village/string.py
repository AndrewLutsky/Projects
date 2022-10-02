#string.py

#import data from rosalind
text = open("rosalind_ini3.txt","rt")
data = text.readlines()
text.close()

string = data[0].strip('\n')

data = data[1].strip('\n')
data = data.split(" ")


#reads text variables into variables
a = int(data[0])
b = int(data[1])
c = int(data[2])
d = int(data[3])


str = ""

str = string[a:b+1] + " " + string[c:d+1]

print(str)

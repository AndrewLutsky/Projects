#reads in data from rosalind
text= open("rosalind_ini5.txt","rt")
data = text.readlines()
text.close()

for i in range(len(data)):
    if i%2 == 1:
        print(data[i].strip('\n'))

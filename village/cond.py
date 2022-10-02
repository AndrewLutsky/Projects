#reads in data from rosalind
text= open("rosalind_ini4.txt","rt")
data = text.read()
text.close()

data = data.split(" ")
a = int(data[0])
b = int(data[1])

sum = 0
for i in range(a,b+1):
    if i%2 == 1:
        sum += i


print(sum)

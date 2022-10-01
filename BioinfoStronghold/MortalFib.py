
#Reads in text data into two variables and casts into integer data type
text = open("rosalind_fibd.txt","rt")
data = text.read()
text.close()



data = data.split(' ')
n=int(data[0])
m=int(data[1])

print(n)
print(m)
#Assigns empty array
#sets first and second index to be 1
arr = [None] * n
arr[0] = 1
arr[1] = 1





#Loops through every month
for i in range(n):
    if i < m and i>1:
        arr[i] = arr[i-1] + arr[i-2]
    if i == m: 
        arr[i] = arr[i-1] + arr[i-2] - arr[i-m]
    if i>m:
        arr[i] = 0
        #sums m-1 terms to find number of rabbits after they die after m months
        for j in range(2,m+1):
            arr[i] = arr[i] + arr[i-j]
            

print(arr)


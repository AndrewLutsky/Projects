#Solution to Rosalind's Consensus and Profile Problem



#import dataset from Rosalind

text = open("Rosalind_cons.txt","rt")
data = text.readlines()
text.close()



#creating a list of the Sequences
Seq = []
count = -1
for line in data:
	if line[0] == ">":
		count += 1
		Seq.append("")
	if line[0] != ">":
		Seq[count] += line.strip('\n')

#Create Matrix with DNA strings

matrix = []
for i in Seq:
	matrix.append(i)



#Create Profile
Profile = []
for j in range(len(matrix[0])):
    countA, countC, countG, countT = 0,0,0,0
    for i in range(len(matrix)):
        if matrix[i][j] == "A":
            countA += 1
        if matrix[i][j] == "C":
            countC += 1
        if matrix[i][j] == "G":
            countG += 1
        if matrix[i][j] == "T":
            countT += 1
    Profile.append([countA,countC,countG,countT])

#Find Consensus Sequence
indexConsensus =[]
for i in Profile:
    indexConsensus.append(i.index(max(i)))

dictIndex = {0:'A', 1:'C',2:'G',3:'T'}

for i in indexConsensus:
    print(dictIndex[i],end="")

#Print the Profile
print("\nA:",end=" ")
for i in Profile:
    print(i[0],end = " ")
print("\nC:",end=" ")
for i in Profile:
    print(i[1],end = " ")
print("\nG:",end=" ")
for i in Profile:
    print(i[2],end = " ")
print("\nT:",end = " ")
for i in Profile:
    print(i[3],end = " ")




        
	


	



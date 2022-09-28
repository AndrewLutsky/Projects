text = open("rosalind_dna.txt","rt")
s = text.read()
text.close()


countA = 0
countB = 0
countC = 0
countD = 0

for i in s:
	if i == "A":
		countA +=1
	if i == "C":
		countB +=1
	if i == "G":
		countC +=1
	if i == "T":
		countD +=1
print(countA,countB,countC,countD)

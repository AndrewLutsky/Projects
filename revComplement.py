text = open("rosalind_revc.txt", "rt")
s = text.read()
text.close()

#reverses the string using slicing
s = s[::-1]
s = s[1:]
#create Dictionary for nucleotides

dic = {"A":"T", "C":"G", "G":"C", "T":"A"}

revComp = ""

for i in s:
	revComp += dic[i]

print(revComp)


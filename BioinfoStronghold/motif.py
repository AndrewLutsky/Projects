text = open("Rosalind_subs.txt","rt")
data = text.readlines()
text.close()


t = data[0].strip('\n')
s = data[1].strip('\n')



for i in range(len(t)):
	if s == t[i:i+len(s)]:
		print(i+1, end = " ")






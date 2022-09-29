text = open("rosalind_hamm.txt", "rt")
data = text.readlines()
text.close()


l = []
for line in data:
	l.append(line.strip('\n'))

s1 = l[0]
s2 = l[1]

count = 0
for j in range(len(s1)):
	if s1[j] != s2[j]:
		count += 1


print(count)

text = open("rosalind_gc.txt", "rt")
data = text.readlines()
data2 = text.read()
text.close()


keys = []
values = []

count = -1
for line in data:
	if line[0] == ">":
		keys.append(line[1:].strip('\n'))
		count += 1
		values.append("")
	if line[0] != ">":
		values[count] += line.strip('\n')
dict = dict(zip(keys,values))

def getGC(s):
	count = 0
	for i in range(len(s)):
		if s[i] == 'G' or s[i] ==  'C':
			count +=1
	
	percent = count/len(s)
	return percent

highest = 0
highestkey = ""
for i in keys:
	if getGC(dict[i]) > highest:
		highestkey = i
		highest = getGC(dict[i])
	

print(highestkey)
print(highest*100)

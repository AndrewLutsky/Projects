text = open("rosalind_data.txt","rt")
s = text.read()
text.close()

t=""
for i in s:
	if i != "T":
		t+=i
	else:
		t+="U"

print(t)

import itertools
text = open("rosalind_lexf.txt","rt")    
s = text.read()    
text.close()

s= s.split('\n')
s.remove('')
alphabet = s[0].replace(' ','')
alphabet = str(alphabet)
number = int(s[1])

final_list = [[]]
length = number
substr = [list(alphabet)] * length
for i in substr:
    final_list = [x+[y] for x in final_list for y in i]
permutations = [''.join(item) for item in final_list]

for i in permutations:
    print(i,end="")
    print("")

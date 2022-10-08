import requests as rq
text = open("Rosalind_mprt.txt", "rt")
data = text.readlines()
text.close()


def hasmotifN(s):
    l1 =[]
    for i in range(len(s)):
        if i<len(s)-3: 
            substr = s[i:i+4]
            if substr[0] == 'N':
                if substr[1] != 'P':
                    if (substr[2] == 'S' or substr[2] == 'T'):
                        if substr[3] !='P':
                            l1.append(i)
    return l1  

for i in data:  
    URL = "http://www.uniprot.org/uniprot/" + str(i.strip('\n')[0:6]) + ".fasta"
    response = rq.get(URL)
    l = str(response.text)
    l = l.split('\n')
    l2 = []
    for j in l:
        if j!='':
            if j[0] == '>':
                l2.append('')
            if j[0] != '>': 
                l2 += j
    s = ''.join(l2)
    a = hasmotifN(s)
    if a != []:
        print(i.strip('\n'))
    for m in a:
        print(m+1,end=' ')
    if a!= []:
        print('\n',end='')

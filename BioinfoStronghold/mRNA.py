text = open("rosalind_mrna.txt","rt")
data = text.read()
text.close


dict =  {     
"UUU":"F","CUU":"L","AUU":"I","GUU":"V","UUC":"F","CUC":"L","AUC":"I","GUC":"V",    
"UUA":"L","CUA":"L","AUA":"I","GUA":"V","UUG":"L","CUG":"L","AUG":"M","GUG":"V",    
"UCU":"S","CCU":"P","ACU":"T","GCU":"A","UCC":"S","CCC":"P","ACC":"T","GCC":"A",    
"UCA":"S","CCA":"P","ACA":"T","GCA":"A","UCG":"S","CCG":"P","ACG":"T","GCG":"A",    
"UAU":"Y","CAU":"H","AAU":"N","GAU":"D","UAC":"Y","CAC":"H","AAC":"N","GAC":"D",    
"UAA":"Stop","CAA":"Q","AAA":"K","GAA":"E","UAG":"Stop","CAG":"Q","AAG":"K","GAG":"E",
"UGU":"C","CGU":"R","AGU":"S","GGU":"G","UGC":"C","CGC":"R","AGC":"S","GGC":"G",    
"UGA":"Stop","CGA":"R","AGA":"R","GGA":"G","UGG":"W","CGG":"R","AGG":"R","GGG":"G"    
}


dict = {v: k for k, v in dict.items()}


dict2 = {"A":4,"C":2,"D":2,"E":2,"F":2,"G":4,"H":2,"I":3,"K":2,"L":6,"M":1,"N":2,"P":4,"Q":2,"R":6,"S":6,"T":4,"V":4,"W":1,"Y":2,"Stop":3}


count = 0
for i in range(len(data.strip('\n'))):
    if i == 1:
        count += dict2[data[i]]
    else:
        count = count * dict2[data[i]]

count = count * dict2["Stop"]
print(count%1000000)
    


text = open("rosalind_orf.txt","rt")
data = text.readlines()
text.close()


#puts the sequence into a string
seq=""
for i in data:
    if i[0] != ">":
        seq += i.strip('\n')

#Creates a dictionary of RNA codes to mRNA
dictCodon =  {         
"UUU":"F","CUU":"L","AUU":"I","GUU":"V","UUC":"F","CUC":"L","AUC":"I","GUC":"V",        
"UUA":"L","CUA":"L","AUA":"I","GUA":"V","UUG":"L","CUG":"L","AUG":"M","GUG":"V",        
"UCU":"S","CCU":"P","ACU":"T","GCU":"A","UCC":"S","CCC":"P","ACC":"T","GCC":"A",        
"UCA":"S","CCA":"P","ACA":"T","GCA":"A","UCG":"S","CCG":"P","ACG":"T","GCG":"A",        
"UAU":"Y","CAU":"H","AAU":"N","GAU":"D","UAC":"Y","CAC":"H","AAC":"N","GAC":"D",        
"UAA":"Stop","CAA":"Q","AAA":"K","GAA":"E","UAG":"Stop","CAG":"Q","AAG":"K","GAG":"E",
"UGU":"C","CGU":"R","AGU":"S","GGU":"G","UGC":"C","CGC":"R","AGC":"S","GGC":"G",
"UGA":"Stop","CGA":"R","AGA":"R","GGA":"G","UGG":"W","CGG":"R","AGG":"R","GGG":"G"    
}    

#Finds the reverse complement of the given DNA strand(if given 5' to 3' returns rev complement in 5' to 3'

def revComp(s):
    dict = {"A":"T", "T":"A","C":"G","G":"C"}
    srev = s[::-1]
    str = ""
    for i in srev:
        str += dict[i]
    
    return str

revSeq = revComp(seq)






#turns a given DNA strand into an RNA strand
def toRNA(s):    
    t=""    
    for i in s:    
        if i != "T":    
            t+=i    
        else:    
            t+="U"    
    return t


#takes sequence and creates codons or list of strings where each string is three chars
def toORF(seq):
    count = 0    
    str = ""    
    listORF = []    
    for i in seq:    
        if count <3:    
            str += i    
            count += 1    	        
        if count == 3:    
            listORF.append(str)    
            str = ""    
            count = 0
    return listORF

#translates ORF to candidate strands
def Translate(seq):
    
    #converts seq to RNA sequence
    seq = str(toRNA(seq))
    #creates ORF codon list
    seqORF = toORF(seq)

    #finds indeces of Methionine
    listIndeces = []
    for i in range(len(seqORF)):
        if dictCodon[seqORF[i]] == "M":
            listIndeces.append(i)
    #creates a list of candidates
    listCand = [None] * len(listIndeces)
    count = 0
    for j in listIndeces:
        listCand[count] = ""
        count += 1
        for k in range(j,len(seqORF)):
            if dictCodon[seqORF[k]] != "Stop":
                listCand[count-1] += dictCodon[seqORF[k]]
            else:
                listCand[count-1] += "-"

    #loops over list of candidates to check if they have a stop codon
    for l in listCand:
        hasStop = False
        for m in l:
            if m == "-":
                hasStop = True
        if hasStop != True:
            listCand.remove(l)
    #Creates an array of valid candidates
    candidates = []
    for n in listCand:
        if n != None:
            cand = []
            startAdding = False
            for o in n:
                if o == "M":
                    startAdding = True
                    cand.append(o)
                if o != "M" and startAdding == True and o!= "-":
                    cand.append(o)
                if o == "-":
                    startAdding = False
                    break
            candidates.append(cand)
    return candidates

#Formatted Print statement
def addFor(s):
    l = []
    for i in Translate(s):
        str =""
        for j in i:
            str += j
        l.append(str)
    return l

l = []
#translates ORF1
l += addFor(seq)
print(l)

#translates ORF2
seq2 = seq[1:]
l += addFor(seq2)
print(l)

#Translates ORF3
seq3 = seq[2:]
l += addFor(seq3)

#translates RevComp ORF1
l += addFor(revSeq)

#Translates RevComp ORF2
revSeq2 = revSeq[1:]
l += addFor(revSeq2)


#Translates RevComp ORF3
revSeq3 = revSeq[2:]
l += addFor(revSeq3)

#creates a list of the candidates and removes duplicates
for i in range(len(l)-1):
    for j in range(len(l)):
        if i != j and l[i] == l[j]:
            l[j] = None
#prints elements that are not none
for x in l:
    if x!= None:
        print(x)

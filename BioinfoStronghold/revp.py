from Bio import SeqIO
#imports record using SeqIO
record = list(SeqIO.parse("rosalind_revp.txt", "fasta"))
seq = record[0].seq

def revComp(s):
    #defines dictionary for complementary sequences
    dict = {"A":"T","T":"A","C":"G","G":"C"}
    rev = s[::-1]
    revComp = ""
    for i in rev:
        revComp += dict[i]
    return revComp


#loops through substring sizes
for i in range(4,13):
    #loops through the main string
    for j in range(len(seq)):
        substr = seq[j:j+i]
#        print(substr, revComp(substr))
        if revComp(substr) == substr:
            if(i + j <= len(seq)):
                print(j+1,i)
            



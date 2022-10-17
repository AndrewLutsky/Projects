from Bio import SeqIO
#imports record using SeqIO
record = list(SeqIO.parse("rosalind_revp.txt", "fasta"))
seq = record[0].seq

#Finds Reverse complement
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
        #finds the substring of length i
        substr = seq[j:j+i]
        #looks to see if the substrings are equal
        if revComp(substr) == substr:
            #looks to see if the index and length of the substring are less 
            #than or equal to the length of the sequence
            if(i + j <= len(seq)):
                print(j+1,i)
            



from Bio import SeqIO
from translate import translate
from DNAtoRNA import DNAtoRNA

#imports first record using SeqIO    
record = list(SeqIO.parse("rosalind_splc.txt", "fasta")) 
primaryseq = record[0]
seqPrimary = primaryseq.seq
seqPrimary = str(seqPrimary)
#loops through stored sequences
for i in record:
    if i is not primaryseq:
        print(str(i.seq))
        seqPrimary = seqPrimary.replace(str(i.seq),"")

#uses DNAtoRNA to create RNA strand
seqPrimary = DNAtoRNA(seqPrimary)

#translates RNA strand to protein sequence
print(translate(seqPrimary))

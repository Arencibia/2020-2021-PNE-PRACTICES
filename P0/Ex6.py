import Seq0

GENE_FOLDER = "./sequences/"
ID = "U5.txt"
U5_seq = Seq0.seq_read_fasta(GENE_FOLDER + ID)

print("------|EXERCISE 6|------")

print("Gene " + ID)
print("Fragment:", U5_seq[0:20])
print("Reverse:", Seq0.seq_reverse(U5_seq[0:20]))

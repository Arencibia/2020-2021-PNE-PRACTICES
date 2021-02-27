import Seq0

GENE_FOLDER = "./sequences/"
ID = "U5.txt"
U5_seq = Seq0.seq_read_fasta(GENE_FOLDER + ID)

print("------|EXERCISE 7|------")

print("Gene " + ID)
print("Frag:", U5_seq[0:20])
print("Rev:", Seq0.seq_complement(U5_seq[0:20]))
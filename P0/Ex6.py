import Seq0

GENE_FOLDER = "./sequences/"
ID = "U5.txt"
number_of_bases = 20
U5_seq = Seq0.seq_read_fasta(GENE_FOLDER + ID)


print("Gene " + ID)
print("Fragment:", U5_seq[0:20])
print("Reverse:", Seq0.seq_reverse(U5_seq[0:20]))

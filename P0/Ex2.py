from Seq0 import seq_read_fasta
FOLDER = "./sequences/"
ID = 'U5.txt'
U5_Seq = seq_read_fasta(FOLDER + ID)

print("------|EXERCISE 2|------")

print('The first 20 bases are: ', U5_Seq[0:20])
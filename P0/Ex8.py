import Seq0

GENE_FOLDER = "./sequences/"
bases = ["A", "C", "T", "G"]
gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

print("-----| Exercise 8 |------")

for gene in gene_list:
    ID = Seq0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
    dict_bases = Seq0.seq_count(ID)
    min_value = 0
    best_base = ""
    for base, value in dict_bases.items():

        while value > min_value:
            min_value = value
            best_base = base
    print("Gene", gene , ": Most frequent Base: ", best_base)
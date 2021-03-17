from Seq1 import Seq

print("-----| Exercise 10 |-----")

FOLDER = "../P0/sequences/"
bases = ["A", "C", "T", "G"]
files_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

for file in files_list:
    s = Seq()
    s.read_fasta(FOLDER + file + ".txt")
    dict_bases = s.count()
    min_value = 0
    best_base = ""
    for base, value in dict_bases.items():

        while value > min_value:
            min_value = value
            best_base = 'a'
    print(f"Gene {file}: Most frequent Base: {best_base}")

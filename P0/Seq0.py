from pathlib import Path

def seq_ping():
    print('OK')

def take_out_first_line(seq):
    return seq[seq.find('\n') + 1:].replace('\n', "")

def seq_read_fasta(filename):
    sequence = take_out_first_line(Path(filename).read_text())
    return sequence
def seq_len(seq):
    return len(seq)

def seq_count_base(seq, base):
    return seq.count(base)
def seq_count(seq):
    gene_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for d in seq:
        gene_dict[d] +=1
    return gene_dict

def seq_reverse(seq):
    return seq[::-1]

def seq_complement(seq):
    bases = ["A", "C", "T", "G"]
    bases_complementary = ["T", "G", "A", "C"]
    dict_bases_complementary = dict(zip(bases, bases_complementary))
    complementary = ""
    for i in seq:
        for base, bases_co in dict_bases_complementary.items():
            if i == base:
                complementary += bases_co

    return complementary 


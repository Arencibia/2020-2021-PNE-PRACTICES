import Seq01

print("-----| Exercise 2 |------")

seq_list = [Seq01.Seq("ACT"), Seq01.Seq("GATA"), Seq01.Seq("CAGATA")]


def print_seqs(seqs):
    for seq in seqs:
        print("Sequence ", seqs.index(seq), ": (Length : ", seq.len(), ")", seq)


print_seqs(seq_list)

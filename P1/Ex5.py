from Seq1 import Seq, test_sequences

print("-----| Exercise 5 |-----")
list_seq = test_sequences()

def print_result(i, sequence):
    print("Sequence " + str(i) + " (Length: " + str(sequence.len()) + "): " + str(sequence))
    a, c, g, t = sequence.count_bases()
    print("A: " + str(a) + ", C: " + str(c) + ", T: " + str(t) + ", G: " + str(g) + ",")


for i in range(0, len(list_seq)):
    print_result(i, list_seq[i - 1])
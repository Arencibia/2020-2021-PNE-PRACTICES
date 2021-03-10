from Seq1 import Seq, test_sequences

print("-----| Exercise 6 |-----")
list_seq = list(test_sequences())


def print_result(i, sequence):
    print("Sequence " + str(i) + " (Length: " + str(sequence.len()) + "): " + str(sequence))
    print("Bases: ", sequence.count())


for i in range(0, len(list_seq)):
    print_result(i, list_seq[i - 1])
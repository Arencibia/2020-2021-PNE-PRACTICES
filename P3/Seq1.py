import termcolor
from pathlib import Path
class Seq:
    NULL_SEQUENCE = 'NULL'
    INVALID_SEQUENCE = 'ERROR'
    def __init__(self, strbases=NULL_SEQUENCE):
       self.strbases = strbases
        if strbases == Seq.NULL_SEQUENCE:
            print('Null seq created')
            self.strbases = strbases
        else:
            if self.is_valid_sequence():
                self.strbases = strbases
                print('New sequence created!')

            else:
                self.strbases = Seq.INVALID_SEQUENCE
                print('INCORRECT sequence detected')
    def is_valid_sequence(self):
        for i in self.strbases:
            if i != 'A' and i != 'C' and i != 'G' and i != 'T':
                return False
        return True

    @staticmethod
    def is_valid_sequence_2(bases):
        for i in strbases:
            if i != 'A' and i != 'C' and i != 'G' and i != 'T':
                return False
        return True
    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            text = 'Sequence' + str(i) + ': (Length:' + str(list_sequences[i].len()) + ')'+ str(list_sequences[i])
            termcolor.cprint(text, 'yellow')
    def __str__(self):

        return self.strbases

    def len(self):

        if self.strbases == Seq.NULL_SEQUENCE or self.strbases == Seq.INVALID_SEQUENCE:
            return 0
        else:
            return len(self.strbases)

    def count_bases(self):
        a, c, g, t = 0, 0, 0, 0
        if not (self.strbases == Seq.NULL_SEQUENCE) and not(self.strbases == Seq.INVALID_SEQUENCE):
            for i in self.strbases:
                if i == 'A':
                    a += 1
                elif i == 'C':
                    c += 1
                elif i == 'G':
                    g += 1
                else:
                    t += 1
        return a, c, g, t
    def count(self):
        a, c, g, t = self.count_bases()
        return {'A': a, 'C': c, 'G': g, 'T': t}

    def reverse(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return 'NULL'
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return 'ERROR'
        else:
            return self.strbases[::-1]

    def complement(self):
        if self.strbases == Seq.NULL_SEQUENCE:
            return Seq.NULL_SEQUENCE
        elif self.strbases == Seq.INVALID_SEQUENCE:
            return Seq.INVALID_SEQUENCE
        else:
            complement = ''
            for i in self.strbases:
                if i == 'A':
                    complement += 'T'
                elif i == 'C':
                    complement += 'G'
                elif i == 'G':
                    complement += 'C'
                elif i == 'T':
                    complement += 'A'
            return complement
    @staticmethod
    def take_out_first_line(sequence):
        return sequence[sequence.find("\n") + 1:].replace("\n","")

    def read_fasta(self, filename):
        self.strbases = Seq.take_out_first_line(Path(filename).read_text())

    def most_frequent_bases(seq):
        gene_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for d in str(seq):
            gene_dict[d] += 1
        freq_base = max(gene_dict, key=gene_dict.get)
        return freq_base

def test_sequences():
    s1 = Seq()
    s2 = Seq('ACTGA')
    s3 = Seq('Invalid Sequence')
    return s1, s2, s3


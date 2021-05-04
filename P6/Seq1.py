from pathlib import Path
import termcolor


class Seq:
    NULL_SEQUENCE = "NULL"
    INVALID_SEQUENCE = "ERROR"

    def __init__(self, str_bases=NULL_SEQUENCE):
        if str_bases == Seq.NULL_SEQUENCE:
            print("NULL seq created.")
            self.str_bases = str_bases
        elif Seq.is_valid_seq2(str_bases):
            self.str_bases = str_bases
            print("New sequence created!")
        else:
            self.str_bases = Seq.INVALID_SEQUENCE
            print("INVALID Seq!")

    @staticmethod
    def is_valid_seq2(str_bases):
        for i in str_bases:
            if i != "A" and i != "C" and i != "G" and i != "T":
                return False
        return True

    @staticmethod
    def print_seqs(seq_list):
        for i in range(0, len(seq_list)):
            text = "Sequence" + str(i) + "(Length: " + str(seq_list[i].len()) + "):" + str(seq_list[i])
            termcolor.cprint(text, "red")

    def is_valid_seq(self):
        for i in self.str_bases:
            if i != "A" and i != "C" and i != "G" and i != "T":
                return False
        return True

    def __str__(self):
        return self.str_bases

    def len(self):
        if self.str_bases == Seq.NULL_SEQUENCE or self.str_bases == Seq.INVALID_SEQUENCE:
            return 0
        else:
            return len(self.str_bases)

    def count_bases(self):
        a, c, g, t = 0, 0, 0, 0
        if not (self.str_bases == Seq.NULL_SEQUENCE) and not (self.str_bases == Seq.INVALID_SEQUENCE):
            for ch in self.str_bases:
                if ch == "A":
                    a += 1
                elif ch == "T":
                    t += 1
                elif ch == "G":
                    g += 1
                elif ch == "C":
                    c += 1
        return a, c, g, t

    def count(self):
        a, c, g, t = self.count_bases()
        return {"A" : a, "C": c, "G" : g, "T" : t}

    def percentaes(self):
        a, c, t, g= self.count_bases()
        per_a="(" + str(round(a/self.len() * 100, 1)) + "%)"
        per_c="(" + str(round(c/self.len() * 100, 1)) + "%)"
        per_t="(" + str(round(t/self.len() * 100, 1)) + "%)"
        per_g="(" + str(round(g/self.len() * 100, 1)) + "%)"
        return "A: " + str(a) + " " + per_a + "\n" + "C: " + str(c) + " " + per_c + "\n" + "T: " + str(t) + " " + per_t + "\n" + "G: " + str(g) + " " + per_g
    def reverse(self):
        if self.str_bases == Seq.NULL_SEQUENCE:
            return "NULL"
        elif self.str_bases == Seq.INVALID_SEQUENCE:
            return "ERROR"
        else:
            return self.str_bases[::-1]

    def complement(self):
        if self.str_bases == Seq.NULL_SEQUENCE:
            return "NULL"
        elif self.str_bases == Seq.INVALID_SEQUENCE:
            return "ERROR"
        else:
            complement = ""
            for ch in self.str_bases:
                if ch == "A":
                    complement += "T"
                elif ch == "T":
                    complement += "A"
                elif ch == "G":
                    complement += "C"
                elif ch == "C":
                    complement += "G"
            return complement

    @staticmethod
    def take_out_first_line(seq):
        return seq[seq.find("\n") + 1:].replace("\n", "")

    def read_fasta(self, filename):
        self.str_bases = Seq.take_out_first_line(Path(filename).read_text())

def seq_frequent(dict_count):
    return max(dict_count, key=dict_count.get)



def test_sequences():
    s1 = Seq()
    s2 = Seq("ACGTA")
    s3 = Seq("Invalid sequence")
    return s1, s2, s3
from Seq1 import Seq


def print_coloured(message, color):
    import termcolor
    """import colorama
    colorama.init(strip="False")"""
    print(termcolor.colored(message, color))


def format_command(command):
    return command.replace("\n", "").replace("\r", "")


def ping(cs):
    print_coloured("PING command!", "green")
    response = "OK!"
    cs.send(str(response).encode())


def get(cs, list_sequences, argument):
    print_coloured("GET", "green")
    response = list_sequences[int(argument)]
    print(response)
    cs.send(str(response).encode())


def info(cs, argument):
    print_coloured("INFO", "green")
    sequence = Seq(argument)
    response = "Sequence: " + str(sequence) + \
               "\nTotal length: " + str(len(str(sequence))) + \
               "\n" + Seq.percentage(sequence)
    print(response)
    cs.send(str(response).encode())


def comp(cs, argument):
    print_coloured("COMP", "green")
    sequence = Seq(argument)
    response = Seq.complement(sequence)
    print(response)
    cs.send(str(response).encode())


def rev(cs, argument):
    print_coloured("REV", "green")
    sequence = Seq(argument)
    response = Seq.reverse(sequence)
    print(response)
    cs.send(str(response).encode())


def gene(cs, argument):
    print_coloured("GENE", "green")
    folder = "./sequences/"
    sequence = Seq()
    sequence.seq_read_fasta(folder + argument + ".txt")
    response = sequence
    print(response)
    cs.send(str(response).encode())

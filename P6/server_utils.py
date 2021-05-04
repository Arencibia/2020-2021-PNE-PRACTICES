from Seq1 import Seq

def print_colored(message, color):
    import termcolor
    import colorama
    colorama.init(strip='False')
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace('\n', "").replace('\r', '')

def ping(cs):
    print_colored('PING command' + '\n', 'green')
    response = 'OK'
    cs.send(str(response).encode())

def get(cs, list_sequences, argument):
    print_colored('GET', 'yellow')
    response = list_sequences[int(argument)] + '\n'
    print(response)
    cs.send(response.encode())

def info(cs, sequence):
    print_colored('INFO', 'red')
    s = Seq(sequence)
    response = 'Total length: ' + str(Seq.len(s)) + "\n" + str(Seq.percentages(s)) + '\n'
    print(response)
    cs.send(response.encode())

def comp(cs, sequence):
    print_colored("COMP", 'blue')
    s = Seq(sequence)
    response = Seq.complement(s) + '\n'
    print(response)
    cs.send(response.encode())

def rev(cs, sequence):
    print_colored("REV", 'green')
    s = Seq(sequence)
    response = Seq.reverse(s) + '\n'
    print(response)
    cs.send(response.encode())

def gene(cs, gene_name):
    FOLDER = "./Sequences/"
    print_colored("GENE", 'yellow')
    s = Seq()
    s.read_fasta(FOLDER + gene_name + ".txt")
    response = str(s) + "\n"
    print(response)
    cs.send(response.encode())
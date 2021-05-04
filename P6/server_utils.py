from Seq1 import Seq
import jinja2
import pathlib

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

def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content

def get(list_sequences, seq_number):
    sequence = list_sequences[int(seq_number)]
    context = {
        "number_sequence": seq_number,
        "sequence": sequence
    }
    contents = read_template_html_file("./html/get.html").render(context=context)
    return contents

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

def gene(gene_name):
    folder = "./sequences/"
    sequence = Seq()
    sequence.seq_read_fasta(folder + gene_name + ".txt")
    context = {
        "gene_name": gene_name,
        "gene_contents": sequence.strbases
    }
    contents = read_template_html_file("./html/gene.html").render(context=context)
    return contents

def correct_sequence(dna):
    for i in dna:
        if i != 'A' and i != 'C' and i != 'G' and i != 'T':
            return False
    return True
def count_bases(dna):
    a, c, g, t= 0, 0, 0, 0
    for i in dna:
        if i == 'A':
            a += 1
        elif i == 'C':
            c += 1
        elif i == 'G':
            g += 1
        else:
            t +=1
    return a, c, g, t
def read_from_file(filename):
    with open(filename, 'r') as f:
        dna= f.read()
        dna= dna.replace('\n', "")
        return dna
dna= read_from_file('dna.txt')
if correct_sequence(dna):
    print('Total length is : ', len(dna))
    a, c, g, t, = count_bases(dna)
    print('A= ', a)
    print('C= ', c)
    print('G= ', g)
    print('T= ', t)
else:
    print('Not a valid sequence')
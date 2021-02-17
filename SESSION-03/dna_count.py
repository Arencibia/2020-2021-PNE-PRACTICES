def correct_sequence(dna):
    for d in dna:
        if d != 'A' and d != 'C' and d != 'G' and d != 'T':
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

dna= input('Introduce the sequence: ')
if correct_sequence(dna):
    print('Total length is : ', len(dna))
    a, c, g, t, = count_bases(dna)
    print('A= ', a)
    print('C= ', c)
    print('G= ', g)
    print('T= ', t)
else:
    print('Not a valid sequence')
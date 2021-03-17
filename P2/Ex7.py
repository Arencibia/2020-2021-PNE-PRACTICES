from  Client0 import Client
from pathlib import Path
from Seq1 import Seq

IP="127.0.0.1"
PORT=10000
PORT2=20000
c= Client(IP,PORT)
c2=Client(IP,PORT2)
s=Seq()
s.read_fasta("../P0/sequences/FRAT1.txt")
count=0
i=0
while i< len (s.str_bases) and count < 5:
    fragment=s.str_bases [i: i+10 ]
    count +=1
    i +=10
    print("Fragment", count, ":" , fragment)
    if count % 2==0:
        print(c2.talk("Fragment " + str(count) + " : " + fragment))
    else:
        print(c.talk("Fragment " + str(count) + " : " + fragment))
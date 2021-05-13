from Client0 import Client

IP = "127.0.0.1"
PORT = 8081

c = Client(IP, PORT)
print("Connection to SERVER at " + IP + ", PORT:" + str(PORT))

print("* Testing PING...")
print(c.talk("PING"), end="\n\n")

print("* Testing GET...")
for i in range(0, 4):
    print("GET " + str(i) + ": " + c.talk("GET " + str(i)))

# Sequence from Get 0
sequence = "AGATCGCGCCACTTCACTGC"

print("\n\n* Testing INFO...")
print(c.talk("INFO " + sequence), end="\n\n")

print("* Testing COMP...")
print("COMP " + sequence + "\n" + c.talk("COMP " + sequence), end="\n\n")

print("* Testing REV...")
print("REV " + sequence + "\n" + c.talk("REV " + sequence), end="\n\n")

gene_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
print("* Testing GENE...")
for gene in gene_list:
    print("GENE " + gene + "\n" + c.talk("GENE " + gene), end="\n\n")
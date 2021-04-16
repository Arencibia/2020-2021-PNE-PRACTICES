from Client0 import Client

list_sequences = ['ACCGTGGTGTAACGAAA', 'ATTTGCTGTCTCT', 'CTCTCTCGAGAGAG', 'TACTCGGCCG', 'CGCGTAGGGATGACGTAGC']
list_genes = ['U5', 'ADA', 'FRAT1', 'FXN', 'RNU6_269P']

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)
print('Connection to SERVER. Client ip, port: ', str(IP) + ',', str(PORT))

print("- Testing ping...")
response = c.talk("ping")
print(f"{response}")

print("- Testing get...")
for n in range(0, len(list_sequences)):
    response = c.talk("get " + str(n))
    print(f"{response}")

print("- Testing info...")
response = c.talk("info " + list_sequences[0])
print(f"{response}")

print("- Testing comp...")
response = c.talk("comp " + list_sequences[0])
print(f"{response}")

print("- Testing rev...")
response = c.talk("rev " + list_sequences[0])
print(f"{response}")

print("- Testing gene...")
for gene in list_genes:
    response = c.talk("gene " + gene)
    print(f"{response}")
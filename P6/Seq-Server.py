import socket
import server_utils

list_sequences = ["AGATCGCGCCACTTCACTGC", "AGCCTCCGCGAAAGAGCGAA", "ACTCCGTCTCAGTAAATAAA", "CTGTACCCGCGTGTTATTTC", "GCCCCCCTCGAAAGTTCCTT"]

# Configure the Server's IP and PORT
PORT = 8085
IP = "127.0.0.1"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")


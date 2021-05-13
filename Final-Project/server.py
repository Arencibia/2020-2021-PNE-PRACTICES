import socket

PORT = 5000
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.bind((IP, PORT))
ls.listen()

print("Server up!")

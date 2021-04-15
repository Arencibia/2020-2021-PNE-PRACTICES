import socket
from termcolor import cprint, colored

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self):
        print("Ok")

    def advanced_ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ip, self.port))
            print("Server is up")
        except ConnectionRefusedError:
            print("Could not connect to the server. Is it running? Have you checked the IP and the Port?")

    def __str__(self):
        return "Connection to SERVER at " + self.ip + ", PORT:" + str(self.port)

    def talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        print("To server:", msg)
        s.send(msg.encode())
        response = s.recv(2048).decode("utf-8")
        s.close()
        return "From server: " + response

    def debug_talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        print("To server:", colored(msg, "blue"))
        s.send(str.encode(msg))
        response = colored(s.recv(2048).decode("utf-8"), "green")
        s.close()
        return "From server: " + response

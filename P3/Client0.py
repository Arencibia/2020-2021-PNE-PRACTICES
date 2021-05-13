import socket


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
            s.close()
        except ConnectionRefusedError:
            print("Could not connect to the server. Is it running? Have you checked the IP and the Port?")

    def __str__(self):
        # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s.connect((self.ip, self.port))
        return "Connection to SERVER at " + self.ip + ", PORT: " + str(self.port)

    def talk(self, msg):
        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))

        # Send data.
        s.send(msg.encode())

        # Receive data
        response = s.recv(2048).decode("utf-8")
        # 2048 number of bytes you can receive at once from the server

        # Close the socket
        s.close()

        # Return the response
        return response

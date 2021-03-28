from Client0 import Client

IP = "127.0.0.1"
PORT = 10000

c = Client(IP, PORT)
print(c)
print()
c.debug_talk("Message 1---")
print()
c.debug_talk("Message 2: Testing!!!")
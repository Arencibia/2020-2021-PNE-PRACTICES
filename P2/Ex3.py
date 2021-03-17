from  Client0 import Client

IP="127.0.0.1"
PORT=10000
c= Client(IP,PORT)
print("Response",c.talk("HELLO I'M THE CLIENT") )
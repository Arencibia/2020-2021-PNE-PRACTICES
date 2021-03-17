from  Client0 import Client
from pathlib import Path

IP="127.0.0.1"
PORT=10000
c= Client(IP,PORT)
print("-----| Exercise 5 |------")
print(c.talk("Sending the U5 file gene to the server"))
print(c.talk(Path("U5.txt").read_text()))
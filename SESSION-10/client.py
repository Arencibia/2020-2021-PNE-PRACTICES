import client0

c = client0.Client("127.0.0.1", 8090)
for i in range(0, 5):
    c.debug_talk("Message " + str(i))
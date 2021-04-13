import socket

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 8080
IP = "127.0.0.1"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()
count = +1

print("The server is configured!")
client_address_list = []
count_connections = 0

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept() #count connections always after accept
        client_address_list.append(client_ip_port)
        count_connections += 1
        print("CONNECTION " + str(count_connections) + ".Client IP, PORT: " + str(client_ip_port))

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:

        print("A client has connected to the server!")

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()

        # -- Print the received message
        print(f"Message received: {msg}")

 # -- Send a response message to the client
        #try is used to avoid the server to stop when something not transformable into an integer is introduced

        try:
            response = int(msg) ** int(msg) #transform the str(msg into integer to operate

        # -- The message has to be encoded into bytes
            cs.send(str(response).encode())# the int is back to a str and encoded into bytes by .encode and sent back to client
        except ValueError:
            cs.send('We need a number'.encode())

        # -- Close the data socket
        cs.close()
        if count_connections == 5:
            for i in range(0, len(client_address_list)):
                print("Client " + str(i) + ": Cilent IP, PORT: " + str(client_address_list[i]))
            break #can also use exit(0), exit(-1): a exit not done properly by the program, exit(0): a proper exit, the program has fully executed, exit(1): program has stopped due to an exception

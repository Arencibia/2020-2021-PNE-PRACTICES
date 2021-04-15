import socket
import server_utils
list_sequence = ["ATTCGATGTGCTAGTCGATGCTGTGTACGTCAGTCAGTCGAT", "CAGTAGATGACGAGCGATGAGCAACCGCATCGAT", "ACGATATAGGAGATATGAGGACACACAATGAGATACA",
     "CAGTACAGATAGAGACATAGATATCACTATACAAAAAAAAAAGTTGAGTA", "CGATACGCAGACTATCGACTAGATATA"]

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

PORT = 9090
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()

print("The server is configured!")
count_connections = 0
client_address_list = []

while True:
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
        client_address_list.append(client_ip_port)
        count_connections += 1
        print("CONNECTION", str(count_connections)+": Client IP, PORT: " + str(client_ip_port))

    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    msg_raw = cs.recv(2048)
    msg = msg_raw.decode()
    formatted_message = server_utils.format_command(msg)
    print(formatted_message)
    formatted_message = formatted_message.split(" ")

    if len(formatted_message) == 1:
        command = formatted_message[0]
    else:
        command = formatted_message[0]
        argument = formatted_message[1]

    if command == "PING":
        server_utils.ping()
        response = "OK!"
        cs.send(str(response).encode())

    elif command == "GET":
        server_utils.print_colored("GET", "yellow")
        response = list_sequence[int(argument)]
        cs.send(str(response + str("\n")).encode())

    else:
        response = "Not available command" + "\n"
        cs.send(str(response).encode())

    cs.close()
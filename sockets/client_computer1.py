#  
#  Auther      : Heinz Samuelsson
#  Date        : ons 23 dec 2015 22:46:45 CET
#  File        : client_computer1.py
#  Reference   : -
#  Description : Client communicating with server_computer2.py
#  Python ver  : 2.7.3 (gcc 4.6.3)

import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ip address and port of server
SERVER_ADDRESS = '192.168.1.66'
PORT           = 33400

clientSocket.connect((SERVER_ADDRESS, PORT))

# send message to server
clientSocket.sendto('Hello from client!', (SERVER_ADDRESS, PORT))

# receive and print message from server
print clientSocket.recv(100)

clientSocket.close

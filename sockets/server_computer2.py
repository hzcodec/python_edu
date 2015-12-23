#  
#  Auther      : Heinz Samuelsson
#  Date        : ons 23 dec 2015 22:46:45 CET
#  File        : client_computer1.py
#  Reference   : -
#  Description : Client communicating with client_computer1.py
#  Python ver  : 2.7.3 (gcc 4.6.3)

import socket
import sys

def main():
  
  serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  port = 33400

  # get hostname of client
  clientHostName = socket.gethostname()
  print 'Client host name: ', clientHostName

  # to get rid of 'Bind failed. Error code: [Errno 98] Address already in use'
  serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_RESUEADDR, 1)

  # get IP address of client
  clientIpAddress = socket.gethostbyame(clientHostName)
  print 'Client IP address: ', clientIpAddress

  # listen to request from other computers
  serverSocket.bind((clientIpAddress, port))
  serverSocket.listen(5)

  chunk = []

  while True:
    # initiate a connection with the client
    clientSocket, addr = serverSocket.accept()
    print 'Connection from ', addr

    chunk = clientSocket.recv(100)
    if not chunk:
      print 'No data was received!'
      break

    print 'Information sent from client: ', chunk

    # send message to client
    clientSocket.send('Message from server.')

    clientSocket.close()

if __name__ == "__main__":
  main()


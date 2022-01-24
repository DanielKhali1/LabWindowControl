import socket
import os
from _thread import *

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0
Clients = []

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)

def sendToAllClients(st):
    for c in Clients:
        c.sendall(str.encode(st))


def threaded_client(connection):
    connection.send(str.encode('Connected to Core'))
    while True:
        data = connection.recv(2048)
        reply = 'Server Says: ' + data.decode('utf-8')
        print(data.decode('utf-8'))
        if not data:
            break
        sendToAllClients(reply)
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    Clients.append(Client)
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()
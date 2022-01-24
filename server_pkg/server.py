import socket
import os
from _thread import *

ServerSocket = socket.socket()

f = open('config.info','r')
lines = f.readlines()

host = lines[0].split(":")[1][:len(lines[0].split(":")[1])-1]
port = int(lines[1].split(":")[1])
print(host, "\n", port)
f.close()

ThreadCount = 0
Clients = []
names = []

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
        comm = input("command: ")
        sendToAllClients(comm)
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    Clients.append(Client)
    name = Client.recv(2048)
    names.append(name.decode('utf-8'))
    print('Connected to: ' + str(name.decode('utf-8')) + ' ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    # ThreadCount += 1
    # print('Thread Number: ' + str(ThreadCount))

ServerSocket.close()
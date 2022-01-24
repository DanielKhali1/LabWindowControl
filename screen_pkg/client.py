import socket


f = open('config.info','r')
lines = f.readlines()

host = lines[0].split(":")[1][:len(lines[0].split(":")[1])-1]
port = int(lines[1].split(":")[1])
name = lines[2].split(":")[1]
print(host, "\n", port, "\n", name)
f.close()
ClientSocket = socket.socket()

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

ClientSocket.send(str.encode(name))
while True:    
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))

ClientSocket.close()
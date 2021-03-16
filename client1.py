from socket import socket
from threading import *
client=socket()

client.bind(("127.0.0.1",2001))

client.connect(("127.0.0.1",4098))

while True:
    print(client.recv(2048).decode())
    client.send(bytes(input(),"utf-8"))
    print(client.recv(2048).decode())
    k=input()
    client.send(bytes(k,"utf-8"))
    if(k=="Y"):
        k=print(client.recv(2048).decode())
        if(type(k)==tuple):
            Thread(connection(k[0],k[1]))
        else:
            while True:
                print(client.recv(2048).decode())
                client.send(bytes(input(),"utf-8"))

    else:
        while True:
                  print(client.recv(2048).decode())
                  client.send(bytes(input(),"utf-8"))

def connection(con,addr):
    pass   
    
client.close()
from socket import socket
from threading import *
from collections import defaultdict
server=socket()

server.bind(("127.0.0.1",4098))

clients=defaultdict(tuple)

server.listen(3)



  
   
def new(con):
    con.send(bytes("Hey what do u want from server","utf=8"))
    while True:
        print(con.recv(2048).decode())
        con.send(bytes(input(),"utf-8"))

    
def connection(con,addr):    
    con.send(bytes("what is your username ?","utf-8"))
    k=con.recv(2048).decode()
    clients[k]=(con,addr)
    con.send(bytes("If u want communicate with other user say Y or N","utf-8"))
    y=con.recv(2048).decode()
    if(y=="Y"):
      con.send(bytes("give the username with whom u want commuinacte","utf-8"))
      k=con.recv(2048).decode()
      for i in clients.keys():
        if(i==k):
            con.send(bytes(str(clients[i][0])+" "+str(clients[i][0]),"utf-8"))
            break
        else:
            pass
      con.send(bytes("There is no such user with that user name","utf-8"))  
      Thread(new(con)).start()
    else:
        Thread(new(con)).start()


while True:
    con,addr=server.accept()
    
    Thread(connection(con,addr)).start()
    
    
    


con.close()
server.close()

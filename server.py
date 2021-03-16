import socket
from threading import *
import time
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import pickle

server=socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(("127.0.0.1",2001))

server.listen(10)
random_generator = Random.new().read
key = RSA.generate(2048, random_generator)
private, public = key, key.publickey()   

def INTERLOCK(con,addr):
    con.send(key.publickey().exportKey(format='PEM', passphrase=None, pkcs=1)) 
    pub=RSA.importKey(con.recv( 2048 ), passphrase=None) 
    while True:
       u=con.recv(256)
       m=key.decrypt(u)
       print(str(m))
       print("write your meassage")
       k=input()
       f=k[:len(k)//2]
       s=k[len(k)//2:]
       enc=pub.encrypt(32,f)
       con.sendall(pickle.dumps(enc))
       if(con.recv(256)):
         mes=con.recv(256)
         print(str(key.decrypt(mes)))
         enc=pub.encrypt(32,f)
         con.sendall(pickle.dumps(enc))    
       

while True:
    con,addr=server.accept()
    INTERLOCK(con,addr)

con.close()
server.close()

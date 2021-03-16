import socket
from threading import *
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import pickle

client=socket.socket()
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


client.bind(("127.0.0.1",8881))

client.connect(("127.0.0.1",2001))
random_generator = Random.new().read
key = RSA.generate(2048, random_generator)
private, public = key, key.publickey()   

def INTERLOCK(con):
    pub=RSA.importKey(con.recv( 2048 ), passphrase=None) 
    con.send(key.publickey().exportKey(format='PEM', passphrase=None, pkcs=1))
    while True:
       print("write your meassage")
       k=input()
       f=k[:len(k)//2]
       s=k[len(k)//2:]
       enc=pub.encrypt(32,f)
       con.sendall(pickle.dumps(enc))
       if(con.recv(256)):
         mes=con.recv(256)
         print(str(key.decrypt(mes)))
         enc=pub.encrypt(32,s)
         con.sendall(pickle.dumps(enc))    
       else:
         client.close()
INTERLOCK(client)
client.close()
import socket
from Pyfhel import Pyfhel,PyCtxt
import os
import time
import threading
import numpy as np

HE = Pyfhel()

HE.contextGen(scheme='bfv',n=2**14,t_bits=40)

HE.keyGen()

HE.save_public_key("mypk.pk")
HE.save_context("mycontext.con")

n=int(input("Enter a integer for computation:"))
integer1=np.array([n])
cx=HE.encryptInt(integer1)
sx=cx.to_bytes()


client =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",9999))

client.sendall(sx)
client.send(b"<END>")




client.close()

def enc():
	file="rd.txt"
	cr=PyCtxt(pyfhel=HE,fileName=file)
	print(f"The result of {integer1}+{integer1} is {cr.decrypt()}")

time.sleep(5)

enc()



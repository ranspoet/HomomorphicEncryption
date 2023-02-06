from Pyfhel import Pyfhel,PyCtxt,PyPtxt
import socket
import sys
import time
import threading


HE_server = Pyfhel()
HE_server.load_context("mycontext.con")
HE_server.load_public_key("mypk.pk")


server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",9999))
server.listen()

client,addt = server.accept()



file_bytes=b""

done=False

while not done:
	data=client.recv(1024)
	if file_bytes[-5:] == b"<END>":
		done = True
	
	else:
			file_bytes+= data

HE_server = Pyfhel()
HE_server.load_context("mycontext.con")
HE_server.load_public_key("mypk.pk")

cx=PyCtxt(pyfhel=HE_server,bytestring=file_bytes[:-5])
cx.save("cipher.txt")
print(type(cx))

sum=cx+cx
print(sys.getsizeof(sum))
sum.save("rd.txt")	



client.close() 




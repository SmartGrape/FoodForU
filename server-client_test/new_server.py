import socket

from _thread import *
import threading 

print_lock = threading.Lock()

def threaded(c):
	while True:
		data = c.recv(1024)
		if not data:
			print("break")
			print_lock.release()
			break
		print(data)
		c.send(data.upper())
	c.close()

def Main():
	host= ''
	port= 8080
	s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host,port))
	print("socket binded to post", port)

	s.listen(5)
	print("socket is listening")

	while True:

		c, addr= s.accept()
		print('Connected to :', addr[0], ':', addr[1])
		start_new_thread(threaded, (c,))
	s.close()


Main()
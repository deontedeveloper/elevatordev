# Original Author: Lonnie Clifton
# Contributors: 
# Date: April 5, 2020
# Revision #: 1.1.1
# Explanation of Recent Changes: Modified document to follow new coding standards.

# Description of Code: ???

import socket
import time
import threading
import sys

# Hi, this is Kent's minor change. Yes it is just a comment, oh well, what can you do? :(
class myThread (threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
	def run(self):
		print ("myListener Starting " + self.name)
		#threadlock.acquire()
		myListener(self)
		#threadlock.release()

	def stop(self):
		print ("udp listener thread exiting")
		exit()
		
def myListener(t):
	UDP_IP = "0.0.0.0" # Listen to all incoming datagrams.
	UDP_PORT = 5005	# To this port.
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP Datagram.
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind((UDP_IP, UDP_PORT))
 
	oldmsg = ""
	
	while True:
		msg, addr = sock.recvfrom(1024)	# Waits for network message, buffer size is 1024 bytes.
		msg = msg.decode('utf-8')	# Change from bytes to 16 bit unicode in utf-8 format.
		ip = addr[0]
		port = addr[1]
		print ('Message received from ', ip)
		print (msg)
		print()
				
def udpListenerStart():
	try:
		threadlock = threading.Lock()
		thread1= myThread(1,"ListenerThread", 1)
		thread1.start()
		print ("udpListenerStart: udp listener thread started")
		#thread1.join()
	except KeyboardInterrupt:
		print ("udpListenerStart- Ctrl+C pressed...")
		sys.exit(0)
    
def send(message, ip, port = 5005):
	messageBytes = message.encode() # Message is broken down into bits to be transmitted over the internet.
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.sendto(messageBytes, (ip, port))
 
udpListenerStart()

# Change the ip address to a RPi running on the network.
ip = "127.0.0.1"  
#ip = '10.81.14.31'
print ('Press ctrl-C twice to exit')
msg="Greetings from " + ip + "!"
while msg != '':
	send(msg, ip)
	print ('msg>', end = '')
	msg = input('msg:')
	

print ('Press ctrl-C to exit network thread')
sys.exit(0)

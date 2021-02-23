# Original Author: Lonnie Clifton
# Contributors: Ariel Merriman
# Date: April 5, 2020
# Revision #: 1.1
# Explanation of Recent Changes: Modified document to follow new coding standards.

# Description of Code: ???

import config
import socket
import time
import threading
import DispatchHandler as dh
import CarLampManager as clm

#from HallButtonCallBack import HallButtonCallBack

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
		if addr == '127.0.0.1':
			print ("got 127.0.0.1")
			pass
		else:
			msg = msg.decode('utf-8') # Change from bytes to 16 bit unicode in utf-8 format.
			ip = addr[0]
			port = addr[1]
			print ('Network Listener received: ', msg, ip)

			if msg.startswith('arrived@floor'):
				msg = msg.replace('arrived@floor|','')	# Remove the handle.
				if oldmsg != msg + ip:
					dh.DispatchHandler(ip, msg)
					oldmsg = msg+ip
				
			elif msg.startswith('stopAtThisFloor|'):
				x = []
				x = msg.split('|')
				floor = int(x[1]) # Imported numbers need to be converted to integers.
				config.CarFloorStopList[floor] = 1
				print ()
				print ('stopAtThisFloor: ', config.CarFloorStopList)
				print ()
			elif msg == 'quit':
				print ("   Network Listener - Received quit message")
				t.stop()

			elif msg == 'MasterIpDiscover':
				if config.Role == 'car':
					time.sleep (2)
				else:
					if config.MasterIpAddress == '0':
						if ip in config.HallCarDictionary:
							pass	# Already present.
						else:
							config.HallCarDictionary = {ip:[0,0,0,0,0,0]}
						print ('  Network Listener - HallCarDictionary: ', config.HallCarDictionary)
						time.sleep(.2)
						msg = "MasterIpOffer"
						config.send (msg, ip, 5006)
						print ("   Network Listener - Discover reply sent to: ", ip)

			elif msg == 'RequestStopInformation':
				# Enter code here to send floor list to car.
				pass

def udpListenerMain():
	try:
		threadlock = threading.Lock()
		thread1= myThread(1,"ListenerThread", 1)
		thread1.start()
		print ("udpListenerMain: udp listener thread started")
		#thread1.join()
	except KeyboardInterrupt:
		print ("udpListenerMain - Ctrl+C pressed...")
		sys.exit(1)
	
#udpListenerMain()

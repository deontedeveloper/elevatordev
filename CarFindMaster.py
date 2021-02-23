# Original Author: Lonnie Clifton
# Contributors: Ariel Merriman
# Date: April 4, 2020
# Revision #: 1.1
# Explanation of Recent Changes: Modified document to follow new coding standards.

# Description of Code: ???

import socket
import time
import config

def sendBroadcast(message, port):
	server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	# Set a timeout so the socket does not block.
	#server.settimeout(0.2)
	server.sendto(message.encode(), ('255.255.255.255', port))
	print("Broadcast Request Sent")

def udpListener(port):
	# Listens for all incoming packets to port.
	UDP_IP = "0.0.0.0"
	UDP_PORT = port
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	# Not using this time as it will throw an exception that must be trapped.
	sock.settimeout(0.4)

	sock.bind((UDP_IP, UDP_PORT))
	data, addr = sock.recvfrom(1024) # Buffer size is 1024 bytes.
	data = data.decode() # Must change from bytes to string.
	return data, addr[0], addr[1] # Address is a tuple of (ip address , port).

def GetMasterIP():
	msg = 'MasterIpDiscover'
	
	sendBroadcast (msg, 5005) # msg and port 5005 are passed as arguments.

	# Loop while waiting for reply.
	count = 0
	while True:
		port = 5006 # Different port used because the normal listener is also listening.
		try:
			msg, ip, port  = udpListener(port)
			#print ("GetMasterIP - Received message:", msg)
			if msg == 'MasterIpOffer':
				print ('GetMasterIP -Master Controller IP address is ', ip)
				config.MasterIpAddress = ip
				return ip
		except socket.timeout:
			print ('GetMasterIP: Socket timeout - retry count: ', count)
			count += 1
			if count > 10:
				return "GetMasterIP - failed to get IP after 10 tries" # Failed to find Master.
			time.sleep (.3) # Wait a short time before trying again.
			sendBroadcast (msg, 5005)
	
# Entry point for this module for testing in isolation.
#GetMasterIP()

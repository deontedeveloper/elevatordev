# Original Author: Lonnie Clifton
# Contributors: Ariel Merriman
# Date: April 5, 2020
# Revision #: 1.1
# Explanation of Recent Changes: Modified document to follow new coding standards.

# Description of Code: This module contains global identifiers and common functions to be imported into modules.

#!/usr/bin/python

import socket
import datetime
import time
DEBUGLEVEL = 3


Role = "" # Hall or Master.

# Car Values.
# Top floor and bottom floor created as variables to allow for changing sizes.

TopFloor = 5
BottomFloor = 1
FloorStopList    = [0,0,0,0,0,0]
CarFloorStopList = [0,0,0,0,0,0]

MasterIpAddress = "0"
MasterPortAddress = 5005

# BCM pin numbers.
#CarLampsPins  = [0,19,20,21,22,23]
#CarButtonPins = [0,14,15,16,17,18]
#LSBottomPin   = 7
#LSTopPin      = 8

# BOARD pin numbers.
CarLampsPins  = [0,35,38,40,15,16]
CarButtonPins = [0,8,10,36,11,12]
LSBottomPin   = 7
LSTopPin      = 8

CarStepWaitTime = .0015

# Master Controller.

StopMetricsDictionary = {}

# Dictionary created to relate IP address to car.
HallCarDictionary = {}
hallCallsUP   = [0,0,0,0,0,0]
hallCallsDOWN = [0,0,0,0,0,0]

def send(message, ip, port = 5005):
	#print ('config.Send: ', ip)
	messageBytes = message.encode() # Message is broken down into bits to be transmitted over the internet.
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.sendto(messageBytes, (ip, port))
	#sock.sendto(message.encode(), (ip, port))

def log(message, level = 1):
	if DEBUGLEVEL > level:
		print (message)
		#sys.stdout.flush()
		ip = '127.0.0.1'
		now = datetime.datetime.now()
		message += str(now) +' | ' + message + ' | ' + MasterIpAddress

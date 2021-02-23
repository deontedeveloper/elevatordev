# Original Author: Lonnie Clifton
# Contributors: Ariel Merriman
# Date: April 5, 2020
# Revision #: 1.1
# Explanation of Recent Changes: Modified document to follow new coding standards.

# Description of Code: This module calls lamp and switch initialization and starts the Network Listener thread.

#!/usr/bin/python3

#import socket
import time
#import config
#import DispatchHandler as dh
from HallLampInitialize import HallLampInitialize
from HallButtonInitialize import HallButtonInitialize
import NetworkListener as nl

def HallManager():
	print ('Starting Hall Manager')
	HallLampInitialize()
	HallButtonInitialize()
	nl.udpListenerMain()
	 
	print ("starting udp listener")
	
	while True:
		time.sleep(.3)
		
	

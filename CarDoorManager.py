# Original Author: Lonnie Clifton
# Contributors: Ariel Merriman
# Date: April 4, 2020
# Revision #: 1.1
# Explanation of Recent Changes: Modified document to follow new coding standards.

# Description of Code: Controls the opening of the car passenger door on arrival at a floor.  Calls CarDoorDriver to interact with the motor.

import time
#import config
from CarDoorDriver import CarDoorDriver

def CarDoorManager(action):
	#doorOpenWaitTime = config.doorOpenWaitTime
	doorOpenWaitTime = 3
	while True:
		# Returns when the door is closed.
		#blockedCount = 0
		
		if action == 'open':
			print ('CarDoorManager: Sending open command')
			CarDoorDriver('open')
			return 'open'
		else:
			print ('CarDoorManager: Sending close command')
			while CarDoorDriver('close') == 'blocked':
				# Door is blocked, keep trying to close.
				#blockedCount += 1
				print ('CarDoorManager: Main: Door is blocked')
				print ('CarDoorManager: Sending Open command')
				CarDoorDriver('open')
				print ('CarDoorManager: Waiting for blocked door timeout')
				time.sleep(doorOpenWaitTime)
				print ('CarDoorDriver: Sending close command')

			return "open"

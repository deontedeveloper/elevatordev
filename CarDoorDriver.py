# Original Author: Lonnie Clifton
# Contributors: Ariel Merriman
# Date: April 4, 2020
# Revision #: 1.1
# Explanation of Recent Changes: Modified document to follow new coding standards.

# Description of Code: Opens or closes the car passenger door.  If the door is closing the object detector will cause the door to (re)open.

#!/usr/bin/python

import time
#import config
import RPi.GPIO as GPIO
#from udpSend import udpSend

# Try to open or close the door and check for door blockage during closing.
def CarDoorDriver(action):

	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	
	# NAME = board port.
	DoorMotorHA1Pin       = 21 
	DoorMotorHA2Pin       = 19
	DoorLimitSwitchOpened = 32
	DoorLimitSwitchClosed = 23
	DoorPeopleDetector    =  3
   
	# Set RPi limit switch so that when closed, the voltage is pulled to zero = false.
	GPIO.setup( DoorLimitSwitchClosed, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup( DoorLimitSwitchOpened, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
	# Set the people detector device so that when its output goes to 5 volts the input detects a true.
	GPIO.setup( DoorPeopleDetector, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
	# Set the H-bridge pin for output.
	GPIO.setup( DoorMotorHA2Pin, GPIO.OUT)
	GPIO.setup( DoorMotorHA1Pin, GPIO.OUT)
	
	# If we set both inputs to the same value so the ridge will have zero ge (???)
	GPIO.output( DoorMotorHA1Pin, False)
	GPIO.output( DoorMotorHA2Pin, False)

	#print ('CarDoorManager: Starting main loop')

	while True:
		if action == 'open':
			# Open the door.
			#print ('CarDoorManager: opening door')
			
			# Turn on the door motor to open.
			GPIO.output(DoorMotorHA1Pin, True)
			GPIO.output(DoorMotorHA2Pin, False)
			
			if not GPIO.input(DoorLimitSwitchOpened):
				# The open limit switch has closed.
				# Input is low/false when switch closes.
				# Stop the door motor.
				GPIO.output(DoorMotorHA1Pin, False)
				GPIO.output(DoorMotorHA2Pin, False)	  
				return 'isOpen' 

		elif action == 'close':
			# Close the door.
			#print ('CarDoorManager: closing door')

			GPIO.output(DoorMotorHA1Pin, False)
			GPIO.output(DoorMotorHA2Pin, True)

			# Check door entry for obstacles.
			if not GPIO.input(DoorPeopleDetector):
				# Detector output will go to 0 volts when blocked.
				# Obstacle detected, stopping motor.
				GPIO.output(DoorMotorHA1Pin, False)
				GPIO.output(DoorMotorHA2Pin, False) 
				return  'isBlocked'

			if not GPIO.input(DoorLimitSwitchClosed) :
				# When door is closed, input is low/false when switch closes.
				GPIO.output(DoorMotorHA1Pin, False)
				GPIO.output(DoorMotorHA2Pin, False)	  
				return 'isClosed'

		time.sleep(.3)
		
	# Turn off the motor.	  
	#GPIO.output(DoorMotoHA1Pin, False)
	#GPIO.output(DoorMotoHA2Pin, False)	  

# This is the main loop for testing.
def TestCarDoor():
	while True:
		blockedCount = 0
		print ('CarDoorDriver: Sending close command')

		while CarDoorDriver('close') == 'blocked':
			# Door is blocked, keep trying to close.
			blockedCount += 1
			print ('CarDoorDriver: Door is blocked --> ', blockedCount)
			print ('CarDoorDriver: Sending Open command')
			status = CarDoorDriver('open')
			print ('CarDoorDriver: Waiting for block timeout')
			time.sleep(5)
			print ('CarDoorDriver: Sending close command')

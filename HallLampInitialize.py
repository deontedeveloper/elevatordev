# Original Author: Lonnie Clifton
# Contributors: 
# Date: April 5, 2020
# Revision #: 1.1
# Explanation of Recent Changse: Modified document to follow new coding standards.

# Description of Code: ???

# TODO
#   Describe this Module
#   Use pin names in config - no magic pin numbers

import RPi.GPIO as GPIO
import time

def HallLampInitialize():

	print ('HallLampInitialize: initialize Starting.....',end="")
	# Use physical pin numbers/GPIO references instead of BCM.
	#GPIO.setmode(GPIO.BOARD)
	
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)

	#HallDownLampPinID = [0,11,12,13,14] # Down.
	#HallDownLampPinID = [0,23,32,33, 8]  # No floor 1 Down.
	
	#HallUpLampPinID   = [0,15,16,17,18] # No floor 5 Up.
	#HallUpLampPinID   = [0,10,36,11,12] # No floor 5 Up.
	
	# Down Lamps setup.
	GPIO.setup(23,GPIO.OUT)
	GPIO.setup(32,GPIO.OUT)
	GPIO.setup(33,GPIO.OUT)
	GPIO.setup( 8,GPIO.OUT)
	
	# Up Lamps setup.
	GPIO.setup(10,GPIO.OUT)
	GPIO.setup(36,GPIO.OUT)
	GPIO.setup(11,GPIO.OUT)
	GPIO.setup(12,GPIO.OUT)

	# Turn on the Down Lamps by pulling the output to ground.
	GPIO.output(23,False)
	GPIO.output(32,False)
	GPIO.output(33,False)
	GPIO.output( 8,False)
	
	# Turn on the Up Lamps.
	GPIO.output(10,False)
	GPIO.output(36,False)
	GPIO.output(11,False)
	GPIO.output(12,False)
	
	time.sleep(2)
	
	# Turn off the Down Lamps.
	GPIO.output(23,True)
	GPIO.output(32,True)
	GPIO.output(33,True)
	GPIO.output( 8,True)
	
	# Turn off the Up Lamps.
	GPIO.output(10,True)
	GPIO.output(36,True)
	GPIO.output(11,True)
	GPIO.output(12,True)

	print ('Complete')

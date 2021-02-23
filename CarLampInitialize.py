# Original Author: Lonnie Clifton
# Contributors: 
# Date: April 4, 2020
# Revision #: 1.1
# Explanation of Recent Changes: Modified document to follow new coding standards.

# Description of Code: Handles turning the elevator car lamps on/off.

import RPi.GPIO as GPIO
import time
import config

def CarLampInitialize():
	print ('CarLampInitialize: begin initialize')
	#CarLampsPins  = [0,19,20,21,22,23] #BCM
	CarLampsPins  = [0,35,38,40,15,16]  #BOARD
	
	# Use physical pin numbers/GPIO references instead of BCM.
	#GPIO.setmode(GPIO.BCM)
	GPIO.setmode(GPIO.BOARD)

	GPIO.setwarnings(False)
	print ("CarLampInitialize start.... ")
	for pin in range(1, config.TopFloor + 1):
		#print (" ", pin, end='')
		GPIO.setup(CarLampsPins[pin],GPIO.OUT)
	
	print()

	# Turn on the car button/lamps.
	for pin in range(1, config.TopFloor + 1):
		GPIO.output(CarLampsPins[pin],False)
	
	# Turn the lamp off after 2 seconds.
	time.sleep(2)

	# Turn off the car button/lamps.
	for pin in range(1, config.TopFloor + 1):
		GPIO.output(CarLampsPins[pin],True)
	
	print ('Car Lamp Initialization Completed.')


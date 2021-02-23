# Original Author: Lonnie Clifton
# Contributors: Ariel Merriman
# Date: April 5, 2020
# Revision #: 1.1
# Explanation of Recent Changes: Modified document to follow new coding standards.

# Description of Code: ???

# Describe this Module.

import RPi.GPIO as GPIO
import time
import config as config

def HallLampManager(floor, status):
	#print ('HallLampManager: ', floor, status)
	# Use physical pin numbers/GPIO references instead of BCM.

	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)

	HallDownLampPinID = [0,23,23,32,33,8]	# Down lamp pin numbers, no floor 1 Down.
	HallUpLampPinID   = [0,10,36,11,12,12]	# Up lamp pin numbers, no top floor up lamp.
	
	# turn off hallway lamps
	for pin in range(1, config.TopFloor + 1):
		GPIO.setup(HallDownLampPinID[pin],GPIO.OUT)
		GPIO.setup(HallUpLampPinID[pin],GPIO.OUT)

	if floor > 0:
		pin = HallUpLampPinID[floor]
		config.hallCallsUP[floor]  = status
	else:
		floor = abs(floor)
		pin = HallDOWNLampPinID[floor]
		config.hallCallsDOWN[floor] = status
	
	if status == 1:
		GPIO.output(pin,False)
	else:
		GPIO.output(pin,True)

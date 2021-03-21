# Original Author: Lonnie Clifton
# Contributors: 
# Date: April 4, 2020
# Revision #: 1.1

# Explanation of Recent Changes: Modified document to follow new coding standards.

# Description of Code: Callback Handler for car button press.  The button pin number is passed to this method,
# the floor stop list is updated, and the lamp is turned on for that floor.

#!/usr/bin/python3

import RPi.GPIO as GPIO
import config

def CarButtonCallBack(buttonID):  
	# All car button presses go here to be handled.
	
	print ("CarButtonCallBack: Button press detected on : ",buttonID)  
	
	# Use physical pin numbers/GPIO references instead of BCM.
	#GPIO.setmode(GPIO.BCM)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)	
	
	floor = config.CarButtonPins.index(buttonID)
	print ('CarButtonCallBack: Floor -->', floor)
	print ('CarButtonCallBack: old CarFloorStopList: ', config.FloorStopList)
	
	# If floor lamp indicator in car is off, turn on and add set list to stop at floor.
	# If floor lamp indicator in car is on, turn off and remove from list.

	lampPin=config.CarLampsPins[floor]
	
	
	if config.CarFloorStopList[floor] == 0:
		config.CarFloorStopList[floor] = 1
		GPIO.output(lampPin,False)
	else:
		config.CarFloorStopList[floor] = 0
		GPIO.output(lampPin, True)
	
	print ('CarButtonCallBack: New CarFloorStopList: ', config.CarFloorStopList)

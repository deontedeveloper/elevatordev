# Original Author: Lonnie Clifton
# Contributors: Evan Ettensohn, Ariel Merriman
# Date: April 5, 2020
# Revision #: 1.1.1
# Explanation of Recent Changes: Modified document to follow new coding standards.

# Description of Code: This module determines when an elevator button is pressed in a hallway and lights the button that was pressed.

# Hall button presses end up here.
# The HallLampInitialize sets up the callbacks.
# Turns on lamp and sets value in config.FloorStopList.

import RPi.GPIO as GPIO
import DispatchHandler as dh
import config

lampPin = 0

def HallButtonCallBack(channel):
	print("HallButtonCallBack: Channel ", channel)

	# Use physical pin numbers/GPIO references instead of BCM.	
	GPIO.setmode(GPIO.BOARD)	
	GPIO.setwarnings(False)
	direction = 1
	
	# These are the channels used for the down buttons.
	buttonsDown = [0, 0, 3, 4, 5, 6]
	buttonsDown = [0, 0, 5, 7,29,31]
	
	# These are the channels used for the up buttons.
	buttonsUp   = [0,  7,  8,  9, 10 ,0]
	buttonsUp   = [0, 26, 24, 21, 19 ,0]
			
	# TODO: Explain what does rising edge refer to?
	# The rising and falling edge function will execute once per program execution while a certain condition is met.
	print ("HallButtonCallBack: Floor request detected on channel: ",channel)  
	floor = 0
	
	# DOWN BUTTONS (there is no floor 1 down button).
	if   channel == 5:
		floor= -2
		lampPin = 23

	elif channel == 7:
		floor= -3
		lampPin = 32

	elif channel == 29:
		floor= -4
		lampPin = 33

	elif channel == 31:
		floor= -5
		lampPin = 8
			
	# UP BUTTONS (there is no floor 5 up button).
	elif   channel ==  26:
		floor=1
		lampPin = 10
		direction = 1
		
	elif channel ==  24:
		floor = 2
		lampPin = 36
		direction = 1
		
	elif channel ==  21:
		floor = 3
		lampPin = 11
		direction = 1
		
	elif channel == 19:
		floor = 4
		lampPin = 12
		direction = 1

	GPIO.output(lampPin,False)		
	
	
	if floor < 0:
		config.hallCallsDOWN[abs(floor)] = 1
		config.hallCallsDOWN[0] = floor
		
	else:
		config.hallCallsUP[floor] = 1
		config.hallCallsUP[0] = floor

	# Display floor number pressed.
	print("HallButtonCallBack: Pressed floor: ", floor)
	print ("HallButtonCallBack - DOWN:  ", config.hallCallsDOWN)
	print ("  HallButtonCallBack - UP:  ", config.hallCallsUP)
	

	dh.UpdateCarStopList()
	

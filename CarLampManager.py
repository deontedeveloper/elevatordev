# Original Author: Lonnie Clifton
# Contributors: 
# Date: April 4, 2020
# Revision #: 1.1
# Explanation of Recent Changes: Modified document to follow new coding standards.


# Description of Code: ???

import time
import RPi.GPIO as GPIO
import config

def CarLampManager(floor, status):
	print ('CarLampManager: ', floor, status)
	#CarLampsPins  = [0,19,20,21,22,23]
	CarLampsPins  = [0,35,38,40,15,16]
	
	# Use physical pin numbers/GPIO references instead of BCM.
	#GPIO.setmode(GPIO.BOARD)
	
	carFloorLamp1 = 35	#19
	carFloorLamp2 = 38	#20
	carFloorLamp3 = 40	#21
	carFloorLamp4 = 15	#22
	carFloorLamp5 = 16	#23
	
	# Set RPi output such that a True (High) outputs +5V to pin.
	# The LED-resistor is connected to ground to compete the circut and turn on the LED.
	
	GPIO.setmode(GPIO.BOARD) # Use pin numbers, not BCM numbers.
	GPIO.setwarnings(False)

	GPIO.setup(carFloorLamp1,GPIO.OUT)
	GPIO.setup(carFloorLamp2,GPIO.OUT)
	GPIO.setup(carFloorLamp3,GPIO.OUT)
	GPIO.setup(carFloorLamp4,GPIO.OUT)
	GPIO.setup(carFloorLamp5,GPIO.OUT)
	
	if floor == 1:
		GPIO.output(carFloorLamp1,True)
		#config.FloorStopList[floor]=status

	if floor == 2:
		GPIO.output(carFloorLamp2,True)
		#config.FloorStopList[floor]=status

	if floor == 3:
		GPIO.output(carFloorLamp3,True)
		#config.FloorStopList[floor]=status

	if floor == 4:
		GPIO.output(carFloorLamp4,True)
		#config.FloorStopList[floor]=status

	if floor == 5:
		GPIO.output(carFloorLamp5,True)
		#config.FloorStopList[floor]=status

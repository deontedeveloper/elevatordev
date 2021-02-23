# Original Author: Lonnie Clifton
# Contributors: 
# Date: April 4, 2020
# Revision #: 1.1
# Explanation of Recent Changes: Modified document to follow new coding standards.

# Description of Code: Controls direction of elevator cars based on calls received.


# TODO:
#   add comments at top of this module the describe the purpose of this module
#   Describe reason for the StepperDriverClass
#   Add recommendations for identifier names
# pip3 install keyboard

#import random
# import keyboard  # using module keyboard
import time
import config
import RPi.GPIO as GPIO

from StepperDriverClass import StepperDriverClass
import CarLampManager as clm
import CarButtonCallBack
import CarButtonInitialize
import CarLampInitialize
import CarFindMaster   as cfm
import CarDoorManager  as cdm
import NetworkListener as nl

import socket

def send(message, ip, port = 5005):
	#print ('Send: ', ip, port)
	messageBytes = message.encode() # message is encoded into byte code for transmission
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.sendto(messageBytes, (ip, port))
	#sock.sendto(message.encode(), (ip, port))

def UpdateMaster(stoplist):
	stringList = 'arrived@floor|'
	# Convert list to CSV string for network transmission.

	stringList += str(stoplist[0]) # Index. 
	for f in range(1, len(stoplist)):
		stringList += ','
		stringList += str(stoplist[f])
	#print ('SendStopList: stringList: ', stringList)
	send(stringList, config.MasterIpAddress)
	
def CarManager():
	topFloor = config.TopFloor
	bottomFloor = config.BottomFloor
	totalSteps = 0
	Car = StepperDriverClass(id, [31,29,7,5], 26, 24 ) # Create an instance of the stepper motor driver.
	
	CarLampInitialize.CarLampInitialize() # Configure GPIO and turn off car lamps.
	CarButtonInitialize.CarButtonInitialize() # Set the car buttons for callbacks	.

	# Clear the floor stop list
	config.CarFloorStopList = [0] * (config.TopFloor + 1) # Create floor stop list, need one more for zero index.
	config.CarFloorStopList[0] = 1 # Set car location to 1 going up.
	
	########cfm.GetMasterIP() # Get the IP address of the Master controller.
	
	#####nl.udpListenerMain()
	
	# cdm.CarDoorManager('close')
	print ('CarManager: Moving to bottom floor')
	# Move car to bottom floor.
	Car.moveCar(-100000)
	time.sleep(.2)
	
	totalSteps = 7400
	#print ('CarManager: Moving to top floor to count steps')
	# Move car to top floor.
	# Will stop when car reaches limit switch.
	totalSteps = Car.moveCar(555555)
	print ("CarManager: Total steps: ", totalSteps)
	#time.sleep(1)
		
	#print ('CarManager: Moving to bottom floor')
	Car.moveCar(-1000000)
	#cdm.CarDoorManager('open')
	
	# Setting parameters for directions, height of elevator, and initial floor.
	#up = 1
	#down = -1
	floor = 1
	direction = 1
	stepsPerFloor = totalSteps / (topFloor - 1)
	currentFloor = 1
	UpdateMaster(config.CarFloorStopList)
	
	# ====================== MAIN LOOP ===============================
	print ('CarManager: Starting main loop')

	while True:
		# Poll the floor call list continuously.
		# The floor poll will look ahead for floors to stop at.
		# If a floor stop is found, the car is "pulled" to that floor.
		# Along the way each floor is checked to see if a new stop has come in,
		# either from inside the car or from the master controller.

		#if keyboard.is_pressed('1'):  # if key '1' is pressed 
		#		CarButtonCallBack(1)
		#	elif keyboard.is_pressed('2'):  # if key '2' is pressed 
		#		CarButtonCallBack(2)
		#	elif keyboard.is_pressed('3'):  # if key '3' is pressed 
		#		CarButtonCallBack(3)
		#	elif keyboard.is_pressed('4'):  # if key '4' is pressed 
		#		CarButtonCallBack(4)
		#	elif keyboard.is_pressed('5'):  # if key '5' is pressed 
		#		CarButtonCallBack(5)

		if config.CarFloorStopList[floor] == 1:
			# The floor being checked may not be where the car is actually currently located.
			# It may be above or below the checked floor.
			while currentFloor != floor:
				# Keep moving car until a stop floor is reached.
				if (floor - currentFloor) > 0:
					# Move car up toward logical floor.
					moveDirection = 1
				else:
					moveDirection = -1

				#cdm.CarDoorManager('close')
				Car.moveCar(stepsPerFloor * moveDirection)	# Move one floor.
				currentFloor += moveDirection			# Now moved, update floor.
				config.CarFloorStopList[0] = currentFloor	# Update list for new floor.
				config.CarFloorStopList[currentFloor] = 0	# Clear list for this floor.
				clm.CarLampManager(currentFloor, 0) 		# Car lamp turned off.
				UpdateMaster(config.CarFloorStopList)
				#if config.CarFloorStopList[currentFloor] == 1:
					# Hall call may happen on the way to the destination floor.
					# Pause at this floor for passengers.
	
		#cdm.CarDoorManager('open')
		#time.sleep(3)
		#cdm.CarDoorManager('close')		
		floor += direction
		
		# Change direction if top or bottom floor reached.
		if floor > topFloor - 1:
			direction = -1
		if floor < bottomFloor + 1: 
			direction = 1
		time.sleep(1)

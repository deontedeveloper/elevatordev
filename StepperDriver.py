# Original Author: Lonnie Clifton
# Contributors: Ariel Merriman
# Date: April 5, 2020
# Revision #: 1.1
# Explanation of Recent Changes: Updated document to follow new coding standards.

# Description of Code: ???

# https://components101.com/motors/28byj-48-stepper-motor 

#  28BYJ-48 Stepper Motor Technical Specifications
#Rated Voltage: 5V DC
#Number of Phases: 4
#Stride Angle: 5.625 degrees/64 = .087875 degrees/step
#Pull in torque: 300 gf.cm
#Insulated Power: 600VAC/1mA/1s
#Coil: Unipolar 5 lead coil

import sys
import time
import RPi.GPIO as GPIO
	
def StepperDriver(moveSteps, waitTime):
	# Use BCM GPIO references instead of physical pin numbers.
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM) # Use logical pin numbers.
	
	# Define pins for limit switch.
	limitSwitchPin = 7 # Physical pin 26.
	GPIO.setup(limitSwitchPin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	
	# Define GPIO signals to use.
	# Physical pins 5, 7, 29, 31.
	# GPIO3, GPIO4, GPIO5, GPIO6.
	stepPins = [3,4,5,6]
	# 3 = orange 1A, 4 = yellow 3B, 29 = pink 2A, 31 = blue 4B.
			                         
	if moveSteps < 0:
		stepDir = 1 # 2 will run faster.
		moveSteps = abs(moveSteps)
	else:
		stepDir = -1 # -2 will run faster.

	# Set all pins to 5 volts (no motor current draw).
	for pin in stepPins:
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin, True)
		
	# Define step sequence per manufacturer's datasheet.
	# Notice that only one bit changes from one pattern to the next.

	# Initialize variables.
	seq =  [[1,0,0,0],
		[1,1,0,0],
		[0,1,0,0],
		[0,1,1,0],
		[0,0,1,0],
		[0,0,1,1],
		[0,0,0,1],
		[1,0,0,1]]

	stepCount = len(seq)
	stepSeqCounter = 0
	currentCount = 0
	startTime = time.time()

	# Start main loop.
	while moveSteps > currentCount:
		for pin in range(0, 4):				# There are 4 pins that control the stepper.
			xpin = stepPins[pin]			# Get the actual pin number.
			if seq[stepSeqCounter][pin] == 1:
				GPIO.output(xpin, False) 	# 0 = 0 volts, coil draws current.
			else:
				GPIO.output(xpin, True) 	# 1 = 5 volts, coil draws no current.
 
		stepSeqCounter += stepDir # Notice that the count will go more than 8 or less than 0.
 
		# When we reach the end of the sequence start again.
		if (stepSeqCounter >= len(seq)):
			stepSeqCounter = 0
		elif (stepSeqCounter < 0):
			stepSeqCounter = len(seq) + stepDir

		endTime = time.time()
		currentCount +=1
		# Check limit switch for closure.
		# Limit Switch Wiring:
		#   Connect switch normally open wires from GPIO pin input to ground.
		#   Connect resistor from GPIO pin input to + 5V.
		#   Switch closure will pull voltage from 5V to ground (pull down).
		if GPIO.input(limitSwitchPin) and currentCount > 100:
			return (endTime - startTime), currentCount, 'Limit Switch'
			exit()
		
		time.sleep(waitTime)		# Wait before moving on.
		
	# Reset ouputs to 5 volts (board indicator lamps will be on.
	# Motor will not draw power because all pins are at 5V (True).
	for pin in stepPins:
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin, True)
		
	return (endTime - startTime), currentCount, 'Counter Limit'
	

# Original Author: Lonnie Clifton
# Contributors: Ariel Merriman
# Date: April 4, 2020
# Revision #: 1.1
# Explanation of Recent Changes: Modified document to follow new coding standards.

# Description of Code: Initializes the car button and sends the input to CarButtonCallBack.py to move the car where it is supposed to go.

#!/usr/bin/python3

# Use pin numbers from config.py as list and configure in loop.

import time
import RPi.GPIO as GPIO
from CarButtonCallBack import CarButtonCallBack

def CarButtonInitialize():
	print ('CarButtonInitialize: initialize ....')

	# Use physical pin numbers/GPIO references instead of BCM.
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)

	# Sets up the pins to to be prepared for an input.
	GPIO.setup(8,  GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
	GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
	GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
	GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
	GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	
	# Detects the push of the button to know what floor the car is being requested to go to from inside the car.
	GPIO.add_event_detect(8,  GPIO.RISING, callback=CarButtonCallBack, bouncetime=400)  
	GPIO.add_event_detect(10, GPIO.RISING, callback=CarButtonCallBack, bouncetime=400)  
	GPIO.add_event_detect(36, GPIO.RISING, callback=CarButtonCallBack, bouncetime=400)  
	GPIO.add_event_detect(11, GPIO.RISING, callback=CarButtonCallBack, bouncetime=400)  
	GPIO.add_event_detect(12, GPIO.RISING, callback=CarButtonCallBack, bouncetime=400)  

	print ('Car buttons initialized for callback.')

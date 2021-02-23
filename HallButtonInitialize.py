# Original Author: Lonnie Clifton
# Contributors: Ariel Merriman
# Date: April 5, 2020
# Revision #: 1.1
# Explanation of Recent Changes: Modified document to follow new coding standards.

# Description of Code: ???

# TODO
#   Describe this Module
#   Use pin names in config - no magic pin numbers

#import time
from HallButtonCallBack import HallButtonCallBack
import RPi.GPIO as GPIO

def HallButtonInitialize():

	print ('HallButton Initialize: Started')
	# Use physical pin numbers/GPIO references instead of BCM.
	#GPIO.setmode(GPIO.BCM)
	
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	
	# Configure the RPi inputs to pull voltage up.
	# A switch closure will pull the input voltage to ground (falling edge).
	# When the switch is opened the output voltage will go up (rising edge).
	
	# Up hall buttons set input mode for pull up event.
	GPIO.setup(5,  GPIO.IN, pull_up_down=GPIO.PUD_UP)  
	GPIO.setup(7,  GPIO.IN, pull_up_down=GPIO.PUD_UP)  
	GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
	GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
	
	# Down.
	GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
	GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
	GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
	GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

	# Up.
	GPIO.add_event_detect(5,  GPIO.RISING, callback=HallButtonCallBack, bouncetime=400)  
	GPIO.add_event_detect(7,  GPIO.RISING, callback=HallButtonCallBack, bouncetime=400)  
	GPIO.add_event_detect(29, GPIO.RISING, callback=HallButtonCallBack, bouncetime=400)  
	GPIO.add_event_detect(31, GPIO.RISING, callback=HallButtonCallBack, bouncetime=400) 
	
	# Down.
	GPIO.add_event_detect(26, GPIO.RISING, callback=HallButtonCallBack, bouncetime=400)  
	GPIO.add_event_detect(24, GPIO.RISING, callback=HallButtonCallBack, bouncetime=400)  
	GPIO.add_event_detect(21, GPIO.RISING, callback=HallButtonCallBack, bouncetime=400)  
	GPIO.add_event_detect(19, GPIO.RISING, callback=HallButtonCallBack, bouncetime=400)  
	
	print ('Hall Buttons Initialization: Completed')

	

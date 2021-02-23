# Original Author: Lonnie Clifton
# Contributors: Ariel Merriman
# Date: April 5, 2020
# Revision #: 1.1
# Explanation of Recent Changes: Modified document to follow new coding standards.

# Description of Code: Determines the role of this RPi by reading jumpers on two inputs.
# This will be updated to have only two roles, Car and Hall, due to change in method to handle multiple elevators.
# Also will free up one I/O port.

#!/usr/bin/python3

import RPi.GPIO    as GPIO
import CarManager  as cm
import HallManager as hm 
import config as config

# Use physical pin numbers/GPIO references instead of BCM.
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Setup RPi device I/O.
# The out pin will be pulled up if true is desired.
rolePinIO = 18
GPIO.setup(rolePinIO,GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Read IO ports if find role.
# Jumper will pull the port to ground (0 Volts) --> false.

print('StartUp: Starting... Detect role of the computer')

if GPIO.input(rolePinIO) == True:
	print ('Input is not jumpered to ground, role is Master.')
	config.Role = 'master'
	hm.HallManager() # HallManager is called
else:
	print ('Input is jumpered to ground, Role is car.')
	config.Role = 'car'
	cm.CarManager() # CarManager is called.


# Python program to test stepper motor driver
# Usage example
#	python TestStepper 4096 .001
#		will rotate motor 4096 steps clockwise with .001 second delay between steps
#		use negative steps to rotate counter clockwise

import StepperDriver as sd
import sys

# Read arguments from command line
if len(sys.argv) > 2:
	steps = int(sys.argv[1])
else:
	steps = 4096	

if len(sys.argv) > 1:
	WaitTime = float(sys.argv[2])
else:
	WaitTime = .001

# Pass parameters to the driver
totalTime, totalSteps, status = sd.StepperDriver( steps, WaitTime)

print ('\n       Total Time:  '+ str(totalTime) +' Seconds')
print (  '        mSec/Step:  ' + str(totalTime/totalSteps * 1000) )
print (  '        Frequency:  ' + str(totalSteps/totalTime) + '  (steps/second)')
print (  '  Degrees rotated:  ' + str(360.0 * (float(totalSteps) / 4096.0)) + '  degrees' )
print (  'Completion Status:  ' + status + '\n')

# CalculateDispatchMetrics.py

#Method to take list of floors to stop and create a new list
  #that reflects the time (metric) for the car to arrive at that
  #floor. The Master Controller will use this list to determine 
  #which car to dispatch to the floor that made the call
  #This method is written to handle any number of floors LC

import time
import config
import socket
import HallLampManager as hlm
import DispatchHandler as dh

def DispatchHandler(ip, msg):
	# This method is called when any car stops at a floor
	# msg arrives as a comma separated string values (CSV)
	# Convert the CSV string to a a list of metric numbers
	print ('DispatchHandler - msg: ',msg)
	
	stopsStr = msg.split(',')
	stopList = []			#create empty list
	print ('DispatchHandler - stopsStr: ', stopsStr)
	
	#------ convert car stop list of string to numbers
	for i in stopsStr:
		stopList.append(int(i))
	floor = stopList[0]
	
	hlm.HallLampManager(floor,0)			# turn off the hall lamp
	if floor < 0:					# clear the hall button pressed lists
		# don't forget the floor is negative if going down
		config.hallCallsDOWN[abs(floor)] = 0
	else:
		config.hallCallsUP[floor] = 0
			
	print('DispatchHandler - stopList: ', stopList)
	
	# convert to metrics list
	x = stopList2Metrics(stopList)
	print ('DispatchHandler - stopList2Metrics: ', x)
	
	# Register this car - add or update the car metrics dictionary
	config.StopMetricsDictionary.update({ip:x})
	print ('config.StopMetricsDictionary: ', config.StopMetricsDictionary)

	UpdateCarStopList()
	
def UpdateCarStopList():
	"""
	Loop through the hall floor calls going up
	 Get the metric of the car Floor for the floor above
	 
	 Check the current floor of each car
	"""
	# Initialize identifiers as string
	# Start with initial metric and find lowest in search do  for
	#  for lowest car metric
	carMetric = 999
	carIP = ""
	bestFloor = 0
		
	for floor in range( 1, len(config.hallCallsUP)):
		#loop through hallCallList
		if  config.hallCallsUP[floor] == 1:
			# This Hall floor button has a call to go up
			
			#Loop through the cars that are registered in the dictionary
			for carIP, car in config.StopMetricsDictionary.items():
				carCurrentFloor = car[0]			# index 0 has this car's floor and directiom
				if car[floor] < carMetric:
					# this car's floor has a lower metric than the last test
					carMetric = car[floor]
					bestFloor = floor

	#loop through the DOWN hallCallList
	for floor in range( 1, len( config.hallCallsDOWN)):
		if config.hallCallsDOWN[floor] == 1:
			# This hallway floor button has a call to go Down
			#Loop through the cars that are registered in the dictionary
			for carIP, car in config.StopMetricsDictionary.items():
				# car is actually a list of floor metrics
				carCurrentFloor = car[floor]			# index 0 has this car's floor and directiom
				if car[floor] < carMetric:
					# this car's floor has a lower metric than the last test
					metcarMetricric = car[floor]
					bestFloor = floor

	print ('    metric: ', carMetric)
	print ('Best Floor: ', bestFloor)
	print ('     carIP: ', carIP)
	if carMetric != 999:
		config.send( 'stopAtThisFloor|' + str(bestFloor),  carIP)
		print('message to stop sent to car: ' , carIP)
		
	#print ('config.StopMetricsDictionary: ', config.StopMetricsDictionary)
	return


def stopList2Metrics(stopList):
	print ('stopList2Metrics: ', stopList)
	# Method used by the cars
	# receives list object of floors calls inside the car
	# returns a list of metric values of the relative time to reach that
	#   floor from its current floor position (list index 0)
	topFloor = config.TopFloor
	bottomFloor = config.BottomFloor
	
	#Create a list for each floor, for 5 floors the length is 6 elements
	list = [0] * len(config.CarFloorStopList)

	# This would work also --> list = [0] * (topFloor - BottomFloor + 2)
	# for 5 floors the list is [0,0,0,0,0,0]
	
	#Check  index 0 to get the car's current floor and direction
	if stopList[0] > 0: 
		direction = 1
	else:
		direction = -1
	
	floor = abs(stopList[0])

	list[0] = stopList[0]  #current floor on now

	metric = 0
	CallListIsEmpty = True  #Assume there are no calls in the this direction
	if direction ==  1:
		# Calc numbers to include top floor
		list[floor] = metric
		for f in range(floor + 1, topFloor + 1):
			metric += 1
			list[f] = metric
			if stopList[f] == 1:  # will be stopping at this floor
				metric += 1
				CallListIsempty = False
				
		if CallListIsEmpty:
			metric = 0
		# Calc numbers from floor BELOW to include bottom floor
		for f in range(floor - 1, bottomFloor - 1, -1):  # Scan going down
			metric += 1
			list[f] = metric
			if stopList[f] == 1:
				metric += 1
		
	else:
		# Direction is down
		# Calc numbers to bottom floor
		CallListIsEmpty = True
		for f in range(floor, bottomFloor - 1, -1):  # Scan list going down
			list[f] = metric
			metric += 1
			if stopList[f] == 1:
				metric += 1
				CallListIsEmpty = False
				
		if CallListIsEmpty: metric = 0
			
		for f in range(floor, topFloor + 1):
			list[f] = metric
			metric += 1
			if stopList[f] == 1:  # will be stopping at this floor
				metric += 1

	return list

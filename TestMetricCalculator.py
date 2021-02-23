"""Temp program to test the CalculateDispatchMetrics module
    will be deleted 
"""
import socket
import time
import config
import udpSend as udp
import CalculateDispatchMetrics as cdm

def send(message, ip, port):
	print (ip, port)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.sendto(message, (ip, port))
	#sock.sendto(message, (ip, port))

config.CarFloorStopList[0] = 5
config.CarFloorStopList[1] = 1
config.CarFloorStopList[2] = 1
config.CarFloorStopList[3] = 1
config.CarFloorStopList[4] = 1
config.CarFloorStopList[5] = 1

print ('Floor Stop List: ', config.CarFloorStopList)

metric = cdm.CalculateDispatchMetrics()
metric = "metric," + metric
print ('  Floor Metrics: ',metric)

message = metric.encode()
print('Encoded in Bytes: ',message)
#send (message, "192.168.254.65", 5005)
udp.Send(message)

# coding: utf-8


import numpy as np
from copy import copy
from sys import argv

script, filename = argv
with open(filename, 'r') as f:
    lines =  f.readlines()
    start = int(lines[0])
    queue = map(int,lines[1].split(','))
    f.close()


def SCAN2(Request, Start, cost):
    length = len(Request)
    Order = []
    location = 0
    point = 0
    x = 0
    Request_tmp = copy(Request)
    Request_tmp.sort()
    
    if (length == 1):
    	if Start >= Request_tmp[0]:
    		cost[0] = cost[0] + Start - Request_tmp[0]
    	else:
    		cost[0] = cost[0] + Request_tmp[0] - Start
        return Request_tmp[0]

    for i in range(length - 1):
    	if Start == Request_tmp[i]:
    		Order.append(Request_tmp[i])
    		del Request_tmp[i]
    		length -= 1
    		x += 1
    		break

    for i in range(length - 1):
    	if (Start >= Request_tmp[i] and Start <= Request_tmp[i+1]):
    		if abs(Start-Request_tmp[i]) <= abs(Start-Request_tmp[i+1]):
    			point = i
    			location = 0
    		else:
    			point = i+1
    			location = 1
    	elif Start > Request_tmp[length-1]:
    		point = length-1
    		location = -1
    	elif Start < Request_tmp[0]:
    		point = 0
    		location = 2

    if location == 0:
    	for i in range(point, -1, -1):
    		Order.append(Request_tmp[i])
    		x += 1
    	for i in range(point+1, length):
    		Order.append(Request_tmp[i])
    		x += 1

    elif location == 1:
    	for i in range(point, length):
    		Order.append(Request_tmp[i])
    		x += 1
    	for i in range(point-1, -1, -1):
    		Order.append(Request_tmp[i])
    		x += 1

    elif location == -1:
    	for i in range(point, -1, -1):
    		Order.append(Request_tmp[i])
    		x += 1

    elif location == 2:
    	for i in range(point, length):
    		Order.append(Request_tmp[i])
    		x += 1

    length1 = len(Order)
    if Start >= Order[0]:
    	cost[0] = cost[0] + Start - Order[0]
    else:
    	cost[0] = cost[0] + Order[0] - Start
    for i in range(length1 - 1):
    	if Order[i] <= Order[i+1]:
    		cost[0] = cost[0] + Order[i+1] -Order[i]
    	else:
    		cost[0] = cost[0] + Order[i] -Order[i+1]

    if location == 0:
    	cost[0] = cost[0] + Request_tmp[0]*2
    elif location == 1:
    	cost[0] = cost[0] + (199 - Request_tmp[length-1])*2

    for i in range(length1):
    	if i == length1 - 1:
    		print Order[i],
    	else:
    		print Order[i],
    		print ",",

    return Order[x-1]

def FSCAN(Request, start):
	cost = []
	cost.append(0)
	length2 = len(Request)

	Request3 = []
	a = length2/10
	b = length2%10

	for i in range(0, a):
		for j in range(0, 10):
			Request3.append(Request[0])
			del Request[0]

		start = SCAN2(Request3, start, cost)
		length4 = len(Request3)
		for k in range(length4):
			del Request3[0]
		if i != a-1 :
			print ",",
		else:
		 	if b == 0:
		 		print "\n",
		 	else:
		 		print ",",

	for i in range(b):
		Request3.append(Request[i])

	if b != 0:
		start = SCAN2(Request3, start,  cost)
		print '\n',

	print cost[0]
	print start,
	print ","
	print cost[0]

FSCAN(queue, start)





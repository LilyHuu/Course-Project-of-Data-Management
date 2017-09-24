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

def SSTF(Request, Start):
    
    Request_tmp = Request
    position = Start
    initial_diff = abs(np.subtract(Start, Request_tmp))
    #highest = max(Request_tmp)
    mindiff = max(initial_diff)
    #j = highest
    Order = []
    cost = 0
    Request_tmp.sort()
    
    while len(Request_tmp) > 0:
        for i in Request_tmp:
            diff = abs(position - i)
            if diff <= mindiff:
                mindiff = diff
                j = i
        if len(Request_tmp) == 1:
            break
        
        cost += abs(position - j)
        position = j
        Request_tmp.remove(j)
        Order.append(j)
        tmp_diff = abs(np.subtract(position, Request_tmp))
        mindiff = max(tmp_diff)
    
    Order.append(j)
    
    cost += abs(position - j)
    longest_wait_request = Order[-1]
    longest_wait_time = cost

    for i in range(len(Order)-1):
        print Order[i], ',',
    print Order[-1]
    print cost
    print longest_wait_request,',', longest_wait_time
  
SSTF(queue, start)
    
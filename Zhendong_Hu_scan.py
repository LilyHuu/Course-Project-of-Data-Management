
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



def SCAN(Request, Start):
    n = len(Request)
    Order = []
    Request_tmp=copy(Request)
    Request_tmp.sort()
    
    for i in range(n-1):
        if (Start >= Request_tmp[i] and Start <= Request_tmp[i+1]):
            queue_point = i
        break
    
    if (abs(Start - Request_tmp[i]) <= abs(Start - Request_tmp[i+1])):
        i = Start - 1
        while i >= 0:
            for j in range(0, n):
                if (Request_tmp[j] == i):
                    Order.append(i)
            i -= 1
        
        k = Start + 1
        while k <= 200:
            for l in range(0, n):
                if (Request_tmp[l] == k):
                    Order.append(k)
            k += 1
        cost = Start + Request_tmp[n-1]
    
    else:
        k = Start + 1
        while k <= 200:
            for l in range(0, n):
                if (Request_tmp[l] == k):
                    Order.append(k)
            k += 1

        i = Start - 1
        while i >= 0:
            for j in range(0, n):
                if (Request_tmp[j] == i):
                    Order.append(i)
            i -= 1
        cost = 199 - Start + 199 - Request_tmp[0]
        
    
    longest_wait_request = Order[-1]
    longest_wait_time = cost

    for i in range(len(Order)-1):
        print Order[i], ',',
    print Order[-1]
    print cost
    print longest_wait_request,',', longest_wait_time
      
SCAN(queue, start)



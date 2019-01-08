# Enter your code here. Read input from STDIN. Print output to STDOUT

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    if len(expenditure) <= d:
        return 0

    counting = [0 for x in range(201)]

    activityNotifications = 0
    for x in expenditure[0:d]:
        counting[x] = counting[x] + 1
    for x in range(d,len(expenditure)):
        med = median(counting, d)
        counting[expenditure[x-d]] = counting[expenditure[x-d]]-1
        counting[expenditure[x]] = counting[expenditure[x]] + 1
        if expenditure[x] >= med * 2:
            activityNotifications = activityNotifications + 1

    return activityNotifications

def median(arr, d):
    half = d//2+1
    even = True if d % 2 == 0 else False
    count = 0
    previous = 0
    for x in range(len(arr)):
        count = count + arr[x]
        if even:
            if count == half-1:
                for y in range(x+1,len(arr)):
                    if arr[y]:
                        return (x + y)/2
            elif count == half and arr[x] == 1:
                return (previous + x)/2
            elif count >= half:
                return x

        else:
            if count >= half:
                return x
        if arr[x]:
            previous = x
        


    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()

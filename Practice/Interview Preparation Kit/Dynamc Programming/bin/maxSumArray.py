#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    biggestValue = [None] * len(arr)
    biggestSum = [None] * len(arr)
    if len(arr) < 3:
        return 0
    biggestValue[0] = arr[0]
    biggestValue[1] = arr[0] if arr[0] > arr[1] else arr[1]
    for x in range(2,len(arr)):
        biggestValue[x] = max([(biggestValue[x-2] + arr[x]), arr[x], biggestValue[x-2], biggestValue[x-1]])
        
        if biggestSum[x-1] == None or biggestValue[x-2] + arr[x] > biggestSum[x-1]:
            biggestSum[x] = biggestValue[x-2] + arr[x]
        else:
            biggestSum[x] = biggestSum[x-1]
                
        ##print(biggestSum)
        #print(biggestValue)

    return max(x for x in biggestSum if x != None)

            
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
